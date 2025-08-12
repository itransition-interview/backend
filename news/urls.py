from django.urls import path
from news import views

urlpatterns = [
    path('', views.NewsAPIView.as_view()),
    path('generate/', views.NewsGenerateAPIView.as_view()),
]