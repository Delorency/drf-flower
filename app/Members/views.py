from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .models import Member
from .serializers import MemberSerializer
from .permissions import MemberChangePermission



class MemberCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,):
	serializer_class = MemberSerializer.CreateSerializer



class MemberListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = MemberSerializer
	queryset = Member.objects.all()

	def get(self, request, id, *args, **kwargs):
		self.queryset = self.queryset.filter()





class MemberUpdateDestroyAPIView(
	generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, MemberChangePermission)
	serializer_class = MemberSerializer.ChangeSerializer
	queryset = Member.objects.all()
	lookup_field = 'id'