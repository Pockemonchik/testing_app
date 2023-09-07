from rest_framework import serializers
from .models import *
from datetime import datetime, date

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id','description','correct')

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id','description','answers')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Test
        fields = ('id', 'theme','description','questions')

class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'theme',)

