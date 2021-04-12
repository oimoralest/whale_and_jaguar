from django.test import TestCase
from api.models import Text
from api.models import Entity


class EntityTestCase(TestCase):
    def setUp(self):
        self.__class__.text = Text.objects.create(
            text='''Barack Obama (born August 4, 1961) is the 44th and current
            President of the United States, and the first African American to
            hold the office.'''
        )
        self.__class__.entity = Entity.objects.create(
            text=self.text,
            date=["August 4, 1961", "44th"],
            location=["United States"],
            keywords=["President", "current", "44th", "United", "August",
                      "African", "American", "Obama", "Barack", "office"],
            person=["Barack Obama"]
            )

    def test_entity_id(self):
        self.assertIsNotNone(self.entity.to_json().get('id'))

    def test_entity_text_id(self):
        entity_text_id = self.entity.to_json().get('text_id')
        text = Text.objects.get(id=entity_text_id)
        self.assertEqual(
            text.to_json().get('id'),
            self.text.to_json().get('id'))
