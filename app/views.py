from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import AudioClip
from .serializers import AudioClipSerializer
# Create your views here.

class AudioClipViewset(viewsets.ModelViewSet):
    queryset = AudioClip.objects.all()
    serializer_class = AudioClipSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['title', 'description']

    def perform_create(self, serializer):
        return serializer.save(uploaded_by=self.request.user)
    
    # def get_queryset(self):
    #     return AudioClip.objects.filter(uploaded_by=self.request.user)
    
    