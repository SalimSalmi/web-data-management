# Movie db

## How to use
Install the requirements.
```
pip install -r requirements.txt
```

Start rest server for postgres
```
python postgres/rest.py
```

Simple request
```
curl -H 'Content-Type: application/json' http://127.0.0.1:5000/movies
```
