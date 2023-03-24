from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, \
RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
DestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend

from utils.custom_permissions import ChangeObjectPermission
from .models import *
from .serializers import *



class ProjectListCreateAPIView(ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectSerializer
	queryset = Project.objects.filter(is_private=False)
	filter_backends = (DjangoFilterBackend,)
	filterset_fields = ('creator', 'workspace')

	def post(self, *args, **kwargs):
		self.serializer_class = self.serializer_class.CreateSerializer
		return super().post(*args, **kwargs)


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, ChangeObjectPermission)
	serializer_class = ProjectSerializer.RetrieveUpdateDestroySerializer
	queryset = Project.objects.all()
	lookup_field = 'id'

	def get(self, request, id):
		self.serializer_class = ProjectSerializer
		return super().get(request)


class ProjectMyListAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectSerializer.MyListSerializer
	queryset = Project.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(creator=request.user)
		return super().get(request)


class ProjectColumnCreateAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectColumnSerializer.CreateSerializer
	queryset = ProjectColumn.objects.all()


class ProjectColumnUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
	permission_classes = (IsAuthenticated, ChangeObjectPermission)
	serializer_class = ProjectColumnSerializer.UpdateDestroySerializer
	queryset = ProjectColumn.objects.all()
	lookup_field = 'id'