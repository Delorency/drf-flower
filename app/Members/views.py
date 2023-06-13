from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .models import Member
from .serializers import MemberSerializer
from .permissions import MemberChangePermission


class MemberMyListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = MemberSerializer
	queryset = Member.objects.all()

	def get(self, request):
		self.queryset = self.queryset.filter(user=request.user)
		return super().get(request)


class MemberRetrieveUpdateDestroyAPIView(
	generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, MemberChangePermission)
	serializer_class = MemberSerializer.ChangeSerializer
	queryset = Member.objects.all()
	lookup_field = 'id'

	def get(self, request, *args, **kwargs):
		self.serializer_class = MemberSerializer
		return super().get(request, *args, **kwargs)