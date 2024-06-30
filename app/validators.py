import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.mp3', '.wav', '.ogg']
    max_file_size = 10 * 1024 * 1024  # 10 MB
    # max_file_size = 10 * 1024  # 10 KB

    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: .mp3, .wav, .ogg')

    if value.size > max_file_size:
        raise ValidationError(f'File size exceeds the limit of 10 MB. Current file size is {value.size / (1024 * 1024):.2f} MB')