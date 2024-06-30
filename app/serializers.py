from rest_framework.serializers import ModelSerializer
from .models import AudioClip

class AudioClipSerializer(ModelSerializer):
    class Meta:
        model = AudioClip
        fields = ['id', 'title', 'description', 'audio_file', 'uploaded_by', 'uploaded_at']
        extra_kwargs = {
            'uploaded_by': {'read_only': True}
            }