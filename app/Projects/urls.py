from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectListCreateAPIView.as_view()),
    path('<int:id>/', views.ProjectUpdateDestroyAPIView.as_view()),
    path('get-<int:id>/', views.ProjectRetrieveAPIView.as_view()),
    path('my/', views.ProjectMyListAPIView.as_view()),
    path('worker/', views.ProjectWorkerListAPIView.as_view()),
    path('all/', views.ProjectAllListAPIView.as_view()),


    path('proposal/', views.ProposalCreateAPIView.as_view()),
    path('proposal/my/', views.ProposalMyListAPIView.as_view()),
    path('proposal/decision/<int:id>/',
        views.ProposalUpdateDestroyAPIView.as_view()),

]
