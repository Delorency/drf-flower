from utils.helpers import CreatorForListSerializerHelper, \
CreatorForCreateSerializerHelper, \
CreatorForChangeSerializerHelper
from .models import *



class WorkspaceSerializer(CreatorForListSerializerHelper):

	class Meta:
		model = Workspace
		fields = '__all__'

	class CreateSerializer(CreatorForCreateSerializerHelper):
		
		def validate(self, attrs):
			attrs['creator'] = self.context['request'].user
			return super().validate(attrs)

		class Meta:
			model = Workspace
			fields = '__all__'
	
	class RetrieveUpdateDestroySerializer(CreatorForChangeSerializerHelper):

		class Meta:
			model = Workspace
			fields = '__all__'