from django.urls import path

from .views import *



urlpatterns = [
	path('', TaskCreateAPIView.as_view()),
	path('my/', TaskMyListAPIView.as_view()),
	path('<int:id>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
	path('change-column/<int:id>/', TaskChangeColumnUpdateAPIView.as_view())
]