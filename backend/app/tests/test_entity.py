from django.test import TestCase
from api.models import Text
from api.models import Entity


class EntityTestCase(TestCase):
    def setUp(self):
        text = Text.objects.create(
            text='''Barack Obama (born August 4, 1961) is the 44th and current
            President of the United States, and the first African American to
            hold the office.'''
        )
        Entity.objects.create(
            text=text,
            date=["August 4, 1961", "44th"],
            location=["United States"],
            keywords=["President", "current", "44th", "United", "August",
                      "African", "American", "Obama", "Barack", "office"],
            person=["Barack Obama"]
            )

    def test_entity_id(self):
        entity = Entity.objects.get().to_json()
        print(entity)
        print(entity.get('text').to_json())
