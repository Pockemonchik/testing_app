from testing import views
from django.urls import re_path
from django.urls import path



urlpatterns = [
    path('tests/<int:pk>/', views.TestDetailView.as_view()),
    path('tests/', views.TestListView.as_view()),
    path('results/', views.TestResultView.as_view()),
]

