from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import loads
from api.models import Text, Sentiment, Entity
import requests
from dotenv import dotenv_values

# Configuration variables to make request to text API
URL = 'https://aylien-text.p.rapidapi.com/'
ENV = dotenv_values('.env')
HEADERS = {
    'x-rapidapi-key': ENV.get('RAPID_API_KEY'),
    'x-rapidapi-host': "aylien-text.p.rapidapi.com"
}


def json_body(body=b''):
    '''This method parses the body content to json content like'''
    try:
        body = body.decode('utf-8')
        json_body = loads(body)
    except Exception as err:
        return {
            'err': err
        }
    return json_body


@csrf_exempt
@require_http_methods(['POST'])
def new_text(request):
    # Check for json content
    if request.headers.get('Content-Type') == 'application/json':
        body = json_body(request.body)
    else:
        return JsonResponse({
            'err': 'Not json content!'
        }, status=404)
    # Request for a sentiment
    sentiment = requests.get(URL + 'sentiment', headers=HEADERS, params=body)
    if sentiment.status_code != 200:
        return JsonResponse(sentiment.json(), status=404)
    # Request for an entity
    entity = requests.get(URL + 'entities', headers=HEADERS, params=body)
    if entity.status_code != 200:
        return JsonResponse(entity.json(), status=404)
    sentiment = sentiment.json()
    entity = entity.json().get('entities')
    # Store the objects in the database
    text = Text.objects.create(
        text=body.get('text')
    )
    sentiment = Sentiment.objects.create(
        text=text,
        polarity=sentiment.get('polarity'),
        subjectivity=sentiment.get('subjectivity'),
        polarity_confidence=sentiment.get('polarity_confidence'),
        subjectivity_confidence=sentiment.get('subjectivity_confidence')
    )
    entity = Entity.objects.create(
        text=text,
        date=entity.get('date'),
        location=entity.get('location'),
        keywords=entity.get('keyword'),
        person=entity.get('person'),
    )
    return JsonResponse({
        'text': text.to_json(),
        'sentiment': sentiment.to_json(),
        'entity': entity.to_json()
    }, status=201)


@require_http_methods(['GET'])
def count_text(request, *args, **kwargs):
    length = int(request.GET.get('count', 10))
    query = Text.objects.order_by('-id')[:length]
    texts, sentiments, entities = [], [], []
    for text in query:
        texts.append(text.to_json())
        sentiment = Sentiment.objects.get(text_id=text.id)
        sentiments.append(sentiment.to_json())
        entity = Entity.objects.get(text_id=text.id)
        entities.append(entity.to_json())
    return JsonResponse({
        'texts': texts,
        'sentiments': sentiments,
        'entities': entities
    })
