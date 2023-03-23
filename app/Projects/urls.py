from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectListCreateAPIView.as_view()),
    path('<int:id>/', views.ProjectRetrieveUpdateDestroyAPIView.as_view()),
    path('my/', views.ProjectMyListAPIView.as_view()),
    
    path('column/', views.ProjectColumnCreateAPIView.as_view()),
    path('column/<int:id>/',
        views.ProjectColumnUpdateDestroyAPIView.as_view()),
]
