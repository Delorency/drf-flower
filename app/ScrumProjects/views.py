from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .permissions import *
from .utils import delete_project
from .models import *
from .serializers import *



class ScrumProjectListCreateAPIView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated, CreatorFieldHelperPermission)
	serializer_class = ScrumProjectSerializer
	queryset = ScrumProject.objects.all()

	def get(self, request, *args, **kwargs):
		self.queryset = self.queryset.filter(is_private=False)
		return super().get(request, *args, **kwargs)

	def post(self, *args, **kwargs):
		self.serializer_class = self.serializer_class.CreateSerializer
		return super().post(*args, **kwargs)



class ScrumProjectMyListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ScrumProjectSerializer
	queryset = ScrumProject.objects.all()

	def get(self, request, *args, **kwargs):
		self.queryset = self.queryset.filter(team__user=request.user)
		return super().get(request, *args, **kwargs)



class ScrumProjectOwnListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ScrumProjectSerializer
	queryset = ScrumProject.objects.all()

	def get(self, request, *args, **kwargs):
		self.queryset = self.queryset.filter(team__user=request.user, role='Project owner')
		return super().get(request, *args, **kwargs)
 


class ScrumProjectRetrieveUpdateDestroyAPIView(
	generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, ProjectChangePermission)
	serializer_class = ScrumProjectSerializer.ChangeSerializer
	queryset = ScrumProject.objects.all()
	lookup_field = 'id'

	def get(self, *args, **kwargs):
		self.serializer_class = ScrumProjectSerializer
		return super().get(*args, **kwargs)

	def perform_destroy(self, instance):
		transaction_handler(delete_project, instance)