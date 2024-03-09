# myapp/tests/test_views.py
import tempfile
import os

from django.test import TestCase
from PIL import Image
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import File 
from ..users.test.factories import UserFactory

class FileViewSetTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.force_authenticate(user=self.user)

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        self.file_data = {'filename': 'test_file', 'file': tmp_file}
        self.url_create = reverse('file-list')

        # Create the file instance
        response = self.client.post(self.url_create, self.file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.file = File.objects.get(id=response.data['id'])
        self.url_detail = reverse('file-detail', args=[self.file.id])

    def tearDown(self):
        # Delete the file instance
        self.file.delete()
        os.remove(f"media{self.file_data['file'].name}")


    def test_retrieve_file(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_file(self):
        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        updated_data = {'filename': 'updated_test_file','file': tmp_file} 
        response = self.client.put(self.url_detail, updated_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
