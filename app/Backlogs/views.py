from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Backlog
from .serializers import BacklogSerializer
from .permissions import BacklogChangePermission



class BacklogCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = BacklogSerializer.CreateSerializer



class BacklogUpdateDestroyAPIView(generics.UpdateAPIView,
	generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, BacklogChangePermission)
	serializer_class = BacklogSerializer.ChangeSerializer
	queryset = Backlog.objects.all()
	lookup_field = 'id'