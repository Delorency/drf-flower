from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *



class ScrumProjectListCreateAPIView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ScrumProjectSerializer
	queryset = ScrumProject.objects.filter(is_private=False)

	def post(self, *args, **kwargs):
		self.serializer_class = self.serializer_class.CreateSerializer
		return super().post(*args, **kwargs)