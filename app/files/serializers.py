from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import File
from ..utils.file_validator import validate_file_extension

import os

class ListFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename', 'description', 'file')
        read_only_fields = ('id',)

class RetrieveFileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = File
        fields = ('id', 'filename', 'description', 'file', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class CreateFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[validate_file_extension])

    class Meta:
        model = File
        fields = ('id', 'filename', 'description', 'file','created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def local_media(self, file):
        tmp = os.path.join(settings.MEDIA_ROOT, "tmp", file.name) 
        path = default_storage.save(tmp, ContentFile(file.read())) # setup BUF SIZE as needed
        return path
    
    def create(self, validated_data):
        file = validated_data.pop('file', None)
        print(file)
        path = self.local_media(file) # use only for local save of the media.
        if file:
            instance = File(**validated_data)
            instance.file = path
            instance.save()
            return instance
        return super().create(validated_data)
    
class PutFileSerializer(CreateFileSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename', 'description','created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')



