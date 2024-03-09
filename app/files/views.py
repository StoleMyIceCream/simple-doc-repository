from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import File
from .serializers import ListFileSerializer, RetrieveFileSerializer, CreateFileSerializer, PutFileSerializer

class FileViewSet(viewsets.ModelViewSet):
                        
    """
    Upload, Update and retrieve files
    """
    serializer_classes = {
        'retrieve': RetrieveFileSerializer,
        'create': CreateFileSerializer,
        'update': PutFileSerializer,
    }
    default_serializer_class = ListFileSerializer # Your default serializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    
    queryset = File.objects.all().order_by('updated_at')
    permission_classes = (IsAuthenticated,)
