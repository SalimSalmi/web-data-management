# Movie db

## How to use
Install the requirements.
```
pip install -r requirements.txt
```

Start rest server for postgres
```
cd postgres
python manage.py runserver
```

Simple request
```
curl -H 'Content-Type: application/json' http://127.0.0.1:8000/movies
```
