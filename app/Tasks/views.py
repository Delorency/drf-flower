from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import *

from .models import *
from .serializers import *



class TaskCreateAPIView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskSerializer.CreateSerializer



class TaskMyListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskSerializer
	queryset = Task.objects.all()

	def get(self, request, *args, **kwargs):
		self.queryset = self.queryset.filter(workers__user=request.user, close=False)
		return super().get(request, *args, **kwargs) 



class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, TaskChangePermission)
	serializer_class = TaskSerializer.UpdateSerializer
	queryset = Task.objects.all()
	lookup_field = 'id'

	def retrieve(self, request, *args, **kwargs):
		self.serializer_class = TaskSerializer
		return super().retrieve(request, *args, **kwargs)



class TaskAddWorkerUpdateAPIView(generics.UpdateAPIView):
	permission_classes = (IsAuthenticated, TaskChangePermission)
	serializer_class = TaskSerializer.AddWorkerSerializer
	queryset = Task.objects.all()
	lookup_field = 'id'



class TaskChangeColumnUpdateAPIView(generics.UpdateAPIView):
	permission_classes = (IsAuthenticated, TaskChangeColumnPermission)
	serializer_class = TaskSerializer.TaskChangeColumnSerializer
	queryset = Task.objects.all()
	lookup_field = 'id'



class TaskItemCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskItemSerializer.CreateSerializer



class TaskItemUpdateDestroyAPIView(generics.UpdateAPIView,
	generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, TaskItemChangePermission)
	serializer_class = TaskItemSerializer.UpdateSerializer
	queryset = TaskItem.objects.all()
	lookup_field = 'id'



class TaskItemChangeCloseUpdateAPIView(generics.UpdateAPIView):
	permission_classes = (IsAuthenticated, TaskItemChangeClosePermission)
	serializer_class = TaskItemSerializer.CloseSerializer
	queryset = TaskItem.objects.all()
	lookup_field = 'id'