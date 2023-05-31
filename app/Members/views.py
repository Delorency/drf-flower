from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .models import Member
from .serializers import MemberSerializer
from .utils import check_member_change_rool



class MemberCreateAPIVIew(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = MemberSerializer.CreateSerializer
	queryset = Member.objects.all()



class MemberRetrieveUpdateDestroyAPIView(
	generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = MemberSerializer.ChangeSerializer
	queryset = Member.objects.all()
	lookup_field = 'id'

	def get(self, *args, **kwargs):
		self.serializer_class = MemberSerializer
		return super().get(*args, **kwargs)

	def perform_destroy(self, instance):
		transaction_handler(check_member_change_rool,
			{'instance':instance, 'user':self.request.user.id})
		return super().perform_destroy(instance)