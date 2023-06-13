from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.permissions import CreatorFieldHelperPermission, \
ProjectUpdatePermission
from utils.decorators import transaction_handler

from .models import *
from .serializers import *
from .utils import delete_sprint
from .permissions import SprintChangePermission



class SprintListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = SprintSerializer
	queryset = Sprint.objects.all()

	def get(self, request, *args, **kwargs):
		self.queryset = self.queryset.filter(
			scrum_project=kwargs.get('id'),
			scrum_project__team__user=request.user)
		return super().get(request)



class SprintCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = SprintSerializer.CreateSerializer



class SprintRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, SprintChangePermission)
	serializer_class = SprintSerializer.UpdateSerializer
	queryset = Sprint.objects.all()
	lookup_field = 'id'

	def get(self, request, *args, **kwargs):
		self.serializer_class = SprintSerializer
		return super().get(request, *args, **kwargs)

	def perform_destroy(self, instance):
		transaction_handler(delete_sprint, instance)