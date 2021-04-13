# Whale_and_Jaguar

## Description

    This is a light app created with Django and React that uses the Text Analysis API to extract the Sentiment and the Entity from a text.

## Content

- [backend app](./backend/app/): REST API created with Django.
- [fronted app](./frontend/app/): Light REACT app to render the last analyzed texts with the API.

## Requirements

- Django
- Python 3.8
- NodeJS
- Postgresql
- Ubuntu 18.04

## Usage

You can clone this repository and install all the requierements

    git clone https://github.com/oimoralest/whale_and_jaguar.git

### backend app (REST API)

To install the requirements just type in your terminal:

    cd backend/app
    pip install -r requirements.txt


I use postgresql as database engine. To install it just type in your terminal:

    sudo apt update && sudo apt-get install -y postgresql postgresql-contrib

Ensure that postgresql service its running:

    sudo service postgresql start

By default postgresql creates a postgres user without password. You can assign it a password:

    sudo psql -U postgres

Inside psql type:

    \password postgres;

By the way, you can create a database to use with Django:

    CREATE DATABASE database_name;
    \q

Before to running the api you will need to define some variables in an .env file inside [backend/app/](./backend/app/) folder:

    PSQL_DB=database_name
    PSQL_USER=database_user_name
    PSQL_PWD=database_user_password
    API_HOST=localhost
    API_PORT=8000
    SECRET_KEY=create_a_secret_key
    RAPID_API_KEY=rapid_api_key

You can get the RAPID_API_KEY from <https://rapidapi.com/aylien/api/text-analysis> creating and account and subscribing to subscribe to test. With the enpoinds you will find the 'x-rapidapi-key'

Also, you need to configure the database applying the Django models. Inside [backend/app/](./backend/app/):

    python manage.py runserver

Now, you can test the API. There are two route availables:

- <http://localhost:8000/api/v1/text>  Accepts POST request with a text inside a json body:

```JSON
{
    "text" = "English text"
}
```

This route returns a JSON with the new content create as follows:

```JSON
{
    "text": {
        "id": int,
        "created_at": datetime.date.now() like format,
        "text":: string,
    },
    "sentiment": {
        "id": int,
        "text_id": int,
        "polarity": string,
        "subjectivity": string,
        "polarity_confidence": float,
        "subjectivity_confidence": float,
    },
    "entity": {
        "id": int,
        "text_id": int,
        "date": array[string],
        "location": array[string],
        "keywords": array[string],
        "person": array[string],
    }
}
```

- <http://localhost:8000/api/v1/text/count> Accepts GET request and returns a JSON as follows:

```JSON
{
    "texts": [
        {
            "id": int,
            "created_at": datetime.date.now() like format,
            "text":: string,
            "sentiment": {
                "id": int,
                "text_id": int,
                "polarity": string,
                "subjectivity": string,
                "polarity_confidence": float,
                "subjectivity_confidence": float,
            },
            "entity": {
                "id": int,
                "text_id": int,
                "date": array[string],
                "location": array[string],
                "keywords": array[string],
                "person": array[string],
            }
        }
    ]
}
```

Also you use count query param for this route to filter the quantity of results that you want to return:

<http://localhost:8000/api/v1/text/count/?count=1>

### frontend app (Ligth React app)

To install the requeriments just type in your terminal:

    cd frontend/app
    npm install

In order to run the app just type:

    npm start

Also you will to run the Django app in other terminal:

    cd backend/app
    python manage.py runserver

You can now go to the following link and enjoy the app:
<http://localhost:3000/>
