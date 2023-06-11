from django.urls import path

from .views import *



urlpatterns = [
	path('', TaskCreateAPIView.as_view()),
	path('my/', TaskMyListAPIView.as_view()),
	path('<int:id>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
	path('change-column/<int:id>/', TaskChangeColumnUpdateAPIView.as_view()),

	path('task-item/', TaskItemCreateAPIView.as_view()),
	path('task-item/<int:id>/', TaskItemUpdateDestroyAPIView.as_view()),
	path('task-item/change-close/<int:id>/', TaskItemChangeCloseUpdateAPIView.as_view()),
]