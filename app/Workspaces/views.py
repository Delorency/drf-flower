from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,\
RetrieveUpdateDestroyAPIView, ListAPIView

from django_filters.rest_framework import DjangoFilterBackend

from utils.custom_permissions import *
from .models import *
from .serializers import WorkspaceSerializer



class WorkspaceListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.filter(is_private=False)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('creator',)

    def post(self, *args, **kwargs):
        self.serializer_class = self.serializer_class.CreateSerializer
        return super().post(*args, **kwargs)


class WorkspaceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ChangeObjectPermission)
    serializer_class = WorkspaceSerializer.RetrieveUpdateDestroySerializer
    queryset = Workspace.objects.all()
    lookup_field = 'id'


class WorkspaceMyListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkspaceSerializer.RetrieveUpdateDestroySerializer
    queryset = Workspace.objects.all()

    def get(self, request):
        self.queryset = self.queryset.filter(creator=request.user)
        return super().get(request)