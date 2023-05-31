from django.urls import path

from .views import *



urlpatterns = [
	path('', MemberCreateAPIVIew.as_view()),
	path('<int:id>/', MemberRetrieveUpdateDestroyAPIView.as_view()),
]
