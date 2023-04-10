from django.urls import path

from . import views


urlpatterns = [
    path('', views.WorkspaceListCreateAPIView.as_view()),
    path('<int:id>/', views.WorkspaceRetrieveUpdateDestroyAPIView.as_view()),
    path('my/', views.WorkspaceMyListAPIView.as_view()),

    path('workspace-projects/<int:id>/', views.ProjectByWorkspace.as_view())
]
