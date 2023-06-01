from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .models import Proposal
from .serializers import ProposalSerializer
from .permissions import ProposalAcceptDeclainPermission



class ProposalCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProposalSerializer.CreateSerializer



class ProposalMyListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProposalSerializer
	queryset = Proposal.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(user=request.user)
		return super().get(request)



class ProposalAcceptDeclainAPIView(generics.UpdateAPIView,
	generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, ProposalAcceptDeclainPermission)
	serializer_class = ProposalSerializer.AcceptDeclainSerializer
	queryset = Proposal.objects.all()
	lookup_field = 'id'