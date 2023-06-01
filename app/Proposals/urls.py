from django.urls import path
from .views import *



urlpatterns = [
	path('', ProposalCreateAPIView.as_view()),
	path('my/', ProposalMyListAPIView.as_view()),
	path('accept-declain/<int:id>/', ProposalAcceptDeclainAPIView.as_view())
]