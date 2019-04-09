# Requirements:
Python 3.7

Postgresql database

environment variable `DATABASE_URL` shall be set to access postgres database
`export DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DBNAME"`

### NOTE
Older python like 3.5 should also be OK.

Postgres is required as I used Django.contrib.postgres.fields package for JSONField

environment variable will be parsed by dj-database-url.

Doc: https://github.com/kennethreitz/dj-database-url

# Running project

### NOTE
Please make sure that `python` path is pointing to python3

## Preparation
`pip install -r requirements.txt`

`./manage.py migrate`

## To run API in debug mode use:
`./manage.py runserver`

## To start fetcher run:
`./manage.py scrapp_res`

### Note
Python command is created in a way that allows it to runs multiple times at onece

Each worker will take care of seperte part of rss changes that we want to fetch.

After that you can access API by calling /v1/data/

