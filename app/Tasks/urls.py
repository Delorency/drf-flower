from django.urls import path

from .views import *



urlpatterns = [
	path('', TaskCreateAPIView.as_view()),
	path('my/', TaskMyListAPIView.as_view()),
	path('<int:id>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
	path('change-workers/<int:id>/', TaskAddWorkerUpdateAPIView.as_view()),
	path('change-column/<int:id>/', TaskChangeColumnUpdateAPIView.as_view()),

	path('task-item/', TaskItemCreateAPIView.as_view()),
	path('task-item/<int:id>/', TaskItemRetrieveUpdateDestroyAPIView.as_view()),
	path('task-item/remove-worker/<int:id>/', TaskItemRemoveWorkerUpdateAPIView.as_view()),
	path('task-item/get-workers/<int:id>/', TaskItemGetWorkersRetrieveAPIView.as_view()),
	path('task-item/change-close/<int:id>/', TaskItemChangeCloseUpdateAPIView.as_view()),
]