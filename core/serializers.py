from rest_framework import serializers
from . import models

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UploadedFiles
        fields = ['id', 'file', 'uploaded_at']
