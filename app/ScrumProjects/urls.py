from django.urls import path

from . import views



urlpatterns = [
    path('', views.ScrumProjectListCreateAPIView.as_view()),
    path('<int:id>/', 
        views.ScrumProjectRetrieveUpdateDestroyAPIView.as_view()),
]
