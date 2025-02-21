from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class APITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('upload')

    def test_invalid_method(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {'error': 'invalid HTTP method'})

    def test_invalid_type_file_post(self):
        file = SimpleUploadedFile(
            'malware.exe',
            b'malware',
            content_type='application/x-msdownload'
        )
        response = self.client.post(self.url, {'file': file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'invalid file type'})
