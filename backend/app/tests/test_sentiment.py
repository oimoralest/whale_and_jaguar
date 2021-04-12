from django.test import TestCase
from api.models import Text
from api.models import Sentiment


class SentimentTestCase(TestCase):
    def setUp(self):
        self.__class__.text = Text.objects.create(
            text='''Barack Obama (born August 4, 1961) is the 44th and current
            President of the United States, and the first African American to
            hold the office.'''
        )
        self.__class__.sentiment = Sentiment.objects.create(
            text=self.text,
            polarity='negative',
            polarity_confidence=0.548789451365,
            subjectivity='parcial',
            subjectivity_confidence=1.0
            )

    def test_sentiment_id(self):
        self.assertIsNotNone(self.sentiment.to_json().get('id'))

    def test_sentiment_text_id(self):
        sentiment_text_id = self.sentiment.to_json().get('text_id')
        text = Text.objects.get(id=sentiment_text_id)
        self.assertEqual(
            text.to_json().get('id'),
            self.text.to_json().get('id'))
