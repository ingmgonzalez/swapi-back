# SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/ingmgonzalez/swapi-back.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server
```
python .\manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
python manage.py test
```

## Url documentación POSTMAN
```
https://documenter.getpostman.com/view/20213440/UVyn1dfz
```
