from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Backlog
from .serializers import BacklogSerializer
from .permissions import BacklogChangePermission



class BacklogListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = BacklogSerializer
	queryset = Backlog.objects.all()

	def get(self, request, **kwargs):
		self.queryset = self.queryset.filter(
			scrum_project=kwargs.get('id'),
			scrum_project__team__user=request.user)

		return super().get(request, **kwargs) 



class BacklogCreateAPIView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = BacklogSerializer.CreateSerializer 



class BacklogUpdateDestroyAPIView(generics.UpdateAPIView,
	generics.DestroyAPIView):
	permission_classes = (IsAuthenticated, BacklogChangePermission)
	serializer_class = BacklogSerializer.ChangeSerializer
	queryset = Backlog.objects.all()
	lookup_field = 'id'