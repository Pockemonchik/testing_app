# from rest_framework.response import Response
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework import status
# from drf_yasg.utils import swagger_auto_schema
# from .serializers import *
# from config.settings import *
# from .models import *
# from config.settings import *
# from core.views import BaseView
# from rest_framework.parsers import MultiPartParser
# from .services import *
# from .tasks import *
# from services import Remanga


# class MangaListView(BaseView, LimitOffsetPagination):
#     """Список мангей или создание манги"""

#     parser_classes = (MultiPartParser,)

#     @swagger_auto_schema(responses={200: MangaSerializer}, query_serializer=MangaQuerySerializer)
#     def get(self, request,source_name):
#         """Возвращает несколько манг в зависимости от параметров"""
#         # проверяем валидность источника
#         if not Source.objects.filter(source_name=source_name):
#             return Response({'error': "Bad source of manga name in url"}, status=status.HTTP_400_BAD_REQUEST)
#         remanga = Remanga()
#         print(remanga.get_daily_top_titles())
#         queryset = Manga.objects.all()
#         paginate_queryset = self.paginate_queryset(queryset, request, view=self)
#         serializer = MangaListSerializer(
#             instance=paginate_queryset, many=True)
#         return self.get_paginated_response(serializer.data)

#     @swagger_auto_schema(responses={200: MangaSerializer}, request_body=MangaSerializer)
#     def post(self, request):
#         """Создание манги"""
#         serializer = MangaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MangaDetailView(BaseView):
#     """Получение, удаление, обновление конкретной манги"""

#     @swagger_auto_schema(responses={200: MangaSerializer})
#     def get(self, request, pk):
#         """Возвращает конкретную мангу"""
#         queryset = Manga.objects.get(id=pk)
#         serializer = MangaSerializer(
#             instance=queryset)
#         return Response(serializer.data)

#     @swagger_auto_schema(responses={200: PutSerializer}, request_body=PutSerializer)
#     def put(self, request, pk):
#         """Полное изменение манги"""
#         record = Manga.objects.get(id=pk)
#         serializer = PutSerializer(
#             record, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         """Изменение парметров манги"""

#         return Response()

#     @swagger_auto_schema(responses={200: MangaSerializer})
#     def delete(self, request, pk):
#         """Удалениие манги из базы"""
#         try:
#             record = Manga.objects.get(id=pk)
#             record.active = False
#             record.save()
#             return Response("delete "+str(pk), status=status.HTTP_200_OK)
#         except:
#             return Response(" cant delete "+str(pk), status=status.HTTP_400_BAD_REQUEST)


# class SourceListView(BaseView, LimitOffsetPagination):
#     """Список источников с мангой"""

#     parser_classes = (MultiPartParser,)

#     @swagger_auto_schema(responses={200: MangaSerializer}, query_serializer=MangaQuerySerializer)
#     def get(self, request,source):
#         """Возвращает список источников манги"""
#         print(source)
#         queryset =Source.objects.all()
#         paginate_queryset = self.paginate_queryset(queryset, request, view=self)
#         serializer = SourceSerializer(
#             instance=paginate_queryset, many=True)
#         return self.get_paginated_response(serializer.data)

