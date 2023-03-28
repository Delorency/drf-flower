from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, \
DestroyAPIView, RetrieveUpdateDestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend

from utils.custom_permissions import ChangeObjectPermission, \
ChangeObjectForTaskCardPermission
from .models import *
from .serializers import *



class ProjectColumnCreateAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectColumnSerializer.CreateSerializer
	queryset = ProjectColumn.objects.all()



class ProjectColumnUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
	permission_classes = (IsAuthenticated, ChangeObjectPermission)
	serializer_class = ProjectColumnSerializer.UpdateDestroySerializer
	queryset = ProjectColumn.objects.all()
	lookup_field = 'id'



class TaskCardCreateAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskCardSerializer.CreateSerializer
	queryset = TaskCard.objects.all()



class TaskCardUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, ChangeObjectForTaskCardPermission)
	serializer_class = TaskCardSerializer.RetrieveUpdateDestroySerializer
	queryset = TaskCard.objects.all()
	lookup_field = 'id'