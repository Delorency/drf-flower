from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.permissions import CreatorFieldHelperPermission, \
ProjectUpdatePermission
from utils.decorators import transaction_handler

from .utils import delete_project
from .models import *
from .serializers import *



class ScrumProjectListCreateAPIView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated, CreatorFieldHelperPermission)
	serializer_class = ScrumProjectSerializer
	queryset = ScrumProject.objects.filter(is_private=False)

	def post(self, *args, **kwargs):
		self.serializer_class = self.serializer_class.CreateSerializer
		return super().post(*args, **kwargs)
 


class ScrumProjectRetrieveUpdateDestroyAPIView(
	generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, ProjectUpdatePermission)
	serializer_class = ScrumProjectSerializer.ChangeSerializer
	queryset = ScrumProject.objects.all()
	lookup_field = 'id'

	def get(self, *args, **kwargs):
		self.serializer_class = ScrumProjectSerializer
		return super().get(*args, **kwargs)

	def perform_destroy(self, instance):
		transaction_handler(delete_project, instance)