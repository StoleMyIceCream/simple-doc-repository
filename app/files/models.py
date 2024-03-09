from django.db import models
from ..utils.models import BaseModel


# Create your models here.
def get_upload_to(instance, filename):
    # for S3 
    pass

class File(BaseModel):
    filename = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=get_upload_to, blank=True, null=True)