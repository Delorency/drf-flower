from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .models import Member
from .serializers import MemberSerializer
from .permissions import MemberChangePermission



class MemberUpdateDestroyAPIView(
	generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, MemberChangePermission)
	serializer_class = MemberSerializer.ChangeSerializer
	queryset = Member.objects.all()
	lookup_field = 'id'