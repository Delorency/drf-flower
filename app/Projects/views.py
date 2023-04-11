from django.db.models import Q
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
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



class ProjectWorkerListAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectSerializer.MyListSerializer
	queryset = Project.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(
			workers=request.user.id
		)
		return super().get(request)


class ProjectAllListAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProjectSerializer.MyListSerializer
	queryset = Project.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(
			Q(workers=request.user.id) | Q(creator=request.user))
		return super().get(request)



class ProposalCreateAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProposalSerializer.CreateSerializer
	queryset = Proposal.objects.all()



class ProposalUpdateDestroyAPIView(APIView):

	def post(self, request, id):
		try:
			with transaction.atomic():
				proposal = Proposal.objects.get(id=id)
				if proposal.user == request.user:
					proposal.project.workers.add(request.user)
					proposal.project.save()
					proposal.delete()

					return Response(status=status.HTTP_204_NO_CONTENT)
				return Response(data={
						"detail": "You do not have permission to perform this action."
						}, status=status.HTTP_403_FORBIDDEN)
		except:
			raise NotFound


	def delete(self, request, id):
		try:
			with transaction.atomic():
				proposal = Proposal.objects.get(id=id)
				if proposal.user == request.user:
					proposal.delete()
					
					return Response(status=status.HTTP_204_NO_CONTENT)
				return Response(data={
						"detail": "You do not have permission to perform this action."
						}, status=status.HTTP_403_FORBIDDEN)
		except:
			raise NotFound




class ProposalMyListAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProposalSerializer
	queryset = Proposal.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(user=request.user)
		return super().get(request)