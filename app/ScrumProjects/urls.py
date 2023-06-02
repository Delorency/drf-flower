from django.urls import path

from .views import *



urlpatterns = [
    path('', ScrumProjectListCreateAPIView.as_view()),
    path('<int:id>/', ScrumProjectRetrieveUpdateDestroyAPIView.as_view())
]