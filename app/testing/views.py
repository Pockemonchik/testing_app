from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from config.settings import *
from .models import *
from config.settings import *
from core.views import BaseView
from .services import *
from django.db.models import Prefetch
from rest_framework.parsers import JSONParser


class TestListView(BaseView):
    """Возвращает список тестов"""

    @swagger_auto_schema(responses={200: TestListSerializer})
    def get(self, request):
        """Возвращает список тестов"""
        queryset = Test.objects.all()
        serializer = TestListSerializer(
            instance=queryset, many=True)
        return Response(serializer.data)


class TestDetailView(BaseView):
    """Возвращает конкретный конкретный тест с вопросами и ответами"""

    @swagger_auto_schema(responses={200: TestSerializer})
    def get(self, request, pk):
        """Возвращает конкретный конкретный тест с вопросами и ответами"""
        queryset = Test.objects.get(id=pk)
        serializer = TestSerializer(
            instance=queryset)
        return Response(serializer.data)


class TestResultView(BaseView):
    """Возвращает результат пройденного теста"""
    parser_classes = (JSONParser,)

    @swagger_auto_schema(request_body=TestSerializer)
    def post(self, request):
        """Принимает id вопроса, список отмеченных ответов, возвращает количество и % правильных ответов"""
        """
       {
            "questions": [{
                    "id": 1,
                    "answers": [1, 2]
                },
                {
                    "id": 2,
                    "answers": [3, 5]
                }
            ]
        }
        
        """
        question_id_list = list(
            map(lambda x: x['id'], request.data['questions']))
        print("question_id_list", question_id_list)

        queryset = Question.objects.filter(id__in=question_id_list)\
            .prefetch_related(Prefetch('answers', queryset=Answer.objects.filter(correct=True)))
        questions = []
        for question in queryset:
            answer_id_list = [answer.id for answer in question.answers.all()]
            questions.append(
                {'id': question.id, 'answers': set(answer_id_list)})

        correct_count = 0
        for question in questions:
            compare_question = list(filter(lambda x: x['id'] == question['id']\
                                            and set(x['answers']) == question['answers'],
                                           request.data['questions']))
            if compare_question:
                correct_count+=1
        correct_persent = int((correct_count/len(questions))*100)
        return Response({'correct_count':correct_count,'correct_persent':correct_persent})
