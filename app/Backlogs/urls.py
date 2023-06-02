from django.urls import path

from .views import * 



urlpatterns = [
	path('', BacklogCreateAPIView.as_view()),
	path('<int:id>/', BacklogUpdateDestroyAPIView.as_view()),
]