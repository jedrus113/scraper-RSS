Requirements:
Python 3.7
Postgresql database
env variable set to postgres://USER:PASSWORD@HOST:PORT/DBNAME

`pip install -r requirements.txt`
`./manage.py migrate`
`./manage.py collectstatic`


to run API in debug mode use:
`./manage.py runserver`

to start fether run:
`./manage.py scrapp_res`
