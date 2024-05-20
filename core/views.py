from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

from .import models
from . import serializers 


# Create your views here.


class UploadedFilesViewset(ModelViewSet):
    queryset = models.UploadedFiles.objects.all()
    serializer_class = serializers.UploadedFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    @action(detail=True, methods=['get'])
    def show(self,request, pk=None):
        uploaded_file = self.get_object()
        path = uploaded_file.file.url
        
        if path.split('.')[-1] == 'jpg':
            return uploaded_file
        
        elif path.split('.')[-1] == 'py':
            # run the python file
            exec(open(path[1:]).read())
            return Response("Done")
            
                            
                            
        