from django.test import Client
from django.test import TestCase


class ViewsTestCase(TestCase):
    def setUp(self):
        self.__class__.text = {
            'text': '''Barack Obama (born August 4, 1961) is the 44th and
            current President of the United States, and the first African
            American to hold the office.'''
        }
        self.__class__.client = Client()

    def no_json_content(self):
        response = self.client.post('/api/v1/text/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('err'), 'Not json content!')

    def test_new_text(self):
        response = self.client.post(
            '/api/v1/text/', self.text, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = response.json()
        self.assertIsNotNone(response.get('text').get('id'))
        self.assertIsNotNone(response.get('sentiment').get('id'))
        self.assertIsNotNone(response.get('entity').get('id'))

    def test_count_text(self):
        self.client.post(
            '/api/v1/text/', self.text, content_type='application/json')
        self.client.post(
            '/api/v1/text/', self.text, content_type='application/json')
        response = self.client.get('/api/v1/text/count/?count=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get('texts')), 1)
        response = self.client.get('/api/v1/text/count/?count=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get('texts')), 2)
