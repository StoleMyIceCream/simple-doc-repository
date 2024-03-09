import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    if value is None:
        raise ValidationError("File is required.")

    _, ext = os.path.splitext(value.name)  
    valid_extensions = []
    return value
    # if ext and not ext.lower() in valid_extensions:
    #     raise ValidationError('Unsupported file extension.')