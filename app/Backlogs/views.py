from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils.decorators import transaction_handler

from .utils import check_user_in_team
from .models import Backlog
from .serializers import BacklogSerializer
from .permissions import BacklogChangePermission



class BacklogListAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = BacklogSerializer
	queryset = Backlog.objects.all()

	def get(self, request, **kwargs):
		transaction_handler(check_user_in_team,
			{
			'scrum_project': kwargs.get('id'),
			'user': request.user
			})
		self.queryset = self.queryset.filter(
			scrum_project__id=kwargs.get('id'))

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