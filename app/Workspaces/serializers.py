from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from Users.serializers import UserSerializer
from .models import *



class WorkspaceSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = Workspace
		fields = ('id', 'name', 'creator', 'is_private', 'created_at')

	class CreateSerializer(CreatorForCreateSerializerHelper):
		
		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			return super().create(attrs)

		class Meta:
			model = Workspace
			fields = '__all__'
	
	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = Workspace
			fields = '__all__'