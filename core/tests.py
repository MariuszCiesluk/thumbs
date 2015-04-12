from django.test import TestCase, RequestFactory
from django.http import Http404

from .views import thumbnail


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_parameters(self):
        request_invalid_size = self.factory.get('/galeria/details')
        
        with self.assertRaises(Http404):
            response = thumbnail(request_invalid_size, "details")

        request_one_size = self.factory.get('/galeria/400')
        with self.assertRaises(Http404):
            response = thumbnail(request_one_size, "400")
        
        request_one_size = self.factory.get('/galeria/400x4r5')
        with self.assertRaises(Http404):
            response = thumbnail(request_one_size, "400x4r5")