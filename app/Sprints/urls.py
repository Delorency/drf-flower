from django.urls import path

from .views import *


urlpatterns = [
	path('get/<int:id>/', SprintListAPIView.as_view()),
	path('<int:id>/', SprintRetrieveUpdateDestroyAPIView.as_view()),
	path('', SprintCreateAPIView.as_view())
]