from django.urls import path

from . import views


urlpatterns = [
    path('', views.TaskCardCreateAPIView.as_view()),
    path('<int:id>/', views.TaskCardUpdateDestroyAPIView.as_view())
]
