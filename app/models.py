from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
# Create your models here.

def upload_file(instance, filename):
    return '/'.join(['audio', instance.uploaded_by.username, filename])

class AudioClip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    audio_file = models.FileField(upload_to=upload_file, validators=[validate_file_extension])
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_clips')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title