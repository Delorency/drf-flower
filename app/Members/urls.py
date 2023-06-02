from django.urls import path

from .views import *



urlpatterns = [
	path('my/', MemberMyListAPIView.as_view()),
	path('<int:id>/', MemberUpdateDestroyAPIView.as_view()),
]
