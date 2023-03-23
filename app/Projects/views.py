from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,\
RetrieveUpdateDestroyAPIView, ListAPIView,CreateAPIView, \
UpdateAPIView, DestroyAPIView

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
	permission_classes = (ChangeObjectPermission,)
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer.RetrieveUpdateDestroySerializer
	lookup_field = 'id'


class ProjectMyListAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer.RetrieveUpdateDestroySerializer

	def get(self, request):
		self.queryset = self.queryset.filter(creator=request.user)
		return super().get(request)


class ProjectColumnCreateAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = ProjectColumn.objects.all()
	serializer_class = ProjectColumnSerializer.CreateSerializer


class ProjectColumnUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
	permission_classes = (ChangeObjectPermission,)
	queryset = ProjectColumn.objects.all()
	serializer_class = ProjectColumnSerializer.UpdateDestroySerializer
	lookup_field = 'id'