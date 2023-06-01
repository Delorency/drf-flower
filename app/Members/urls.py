from django.urls import path

from .views import *



urlpatterns = [
	path('<int:id>/', MemberUpdateDestroyAPIView.as_view()),
]
