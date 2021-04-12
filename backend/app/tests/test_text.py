from django.test import TestCase
from api.models import Text
from datetime import date


class TextTestCase(TestCase):
    def setUp(self):
        Text.objects.create(
            text='''Difficulty on insensible reasonable in. From as went he
            they. Preference themselves me as thoroughly partiality considered
            on in estimating. Middletons acceptance discovered projecting so is
            so or. In or attachment inquietude remarkably comparison at an. Is
            surrounded prosperous stimulated am me discretion expression. But
            truth being state can she china widow. Occasional preference fat
            remarkably now projecting uncommonly dissimilar. Sentiments
            projection particular companions interested do at my delightful.
            Listening newspaper in advantage frankness to concluded unwilling.
            '''
        )

    def test_text_id(self):
        text = Text.objects.get().to_json()
        self.assertIsNotNone(text.get('id'))

    def test_text_created_at(self):
        text = Text.objects.get().to_json()
        self.assertEqual(text.get('created_at'), date.today())
