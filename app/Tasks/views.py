from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import *

from .models import *
from .serializers import *



class TaskCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskSerializer.CreateSerializer



class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, TaskChangePermission)
	serializer_class = TaskSerializer.UpdateSerializer
	queryset = Task.objects.all()
	lookup_field = 'id'

	def retrieve(self, request, *args, **kwargs):
		self.serializer_class = TaskSerializer
		return super().retrieve(request, *args, **kwargs)



class TaskChangeColumnUpdateAPIView(generics.UpdateAPIView):
	permission_classes = (IsAuthenticated, TaskChangeColumnPermission)
	serializer_class = TaskSerializer.TaskChangeColumnSerializer
	queryset = Task.objects.all()
	lookup_field = 'id'