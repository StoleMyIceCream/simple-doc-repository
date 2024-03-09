import uuid
from django.db import  models
from django.db.models import F

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def get_relationship_fields(self):
        return {field.name: list(field.related_model._meta.get_fields()) for field in self._meta.related_objects}

    def create_relationship_annotate_field_names(self):
        return {k: {f"{k[:-1] if k.endswith('s') else k}_{field.name}": F(f"{k}__{field.name}") for field in v}
                for k, v in self.get_relationship_fields().items()}