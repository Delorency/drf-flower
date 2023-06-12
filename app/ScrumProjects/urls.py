from django.urls import path

from .views import *



urlpatterns = [
    path('', ScrumProjectListCreateAPIView.as_view()),
    path('my/', ScrumProjectMyListAPIView.as_view()),
    path('own/', ScrumProjectOwnListAPIView.as_view()),
    path('<int:id>/', ScrumProjectRetrieveUpdateDestroyAPIView.as_view()),
]
