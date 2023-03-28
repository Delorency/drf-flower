from django.urls import path

from . import views


urlpatterns = [
    path('', views.TaskCardCreateAPIView.as_view()),
    path('<int:id>/', views.TaskCardUpdateDestroyAPIView.as_view()),

    path('column/', views.ProjectColumnCreateAPIView.as_view()),
    path('column/<int:id>/',
        views.ProjectColumnUpdateDestroyAPIView.as_view()),
]
