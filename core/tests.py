from django.test import TestCase, RequestFactory

from .views import my_view


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_parameters(self):
        request_invalid_size = self.factory.get('/galeria/details')
        response = my_view(request_invalid_size)
        self.assertEqual(response.status_code, 404)

        request_one_size = self.factory.get('/galeria/400')
        response = my_view(request_one_size)
        self.assertEqual(response.status_code, 404)
        
        request_one_size = self.factory.get('/galeria/400x4r5')
        response = my_view(request_one_size)
        self.assertEqual(response.status_code, 404)