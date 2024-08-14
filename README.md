# Init API for this project

`$ make clean`

`$ make migrations`

`$ make migrations-appointments`

`$ make migrate`

`$ make superuser`

`$ make run`

# Migrate command

```
make migrate
```

# migrations command

```
make migrations
```

or (`appointments` is an app for this project)

```
make migrations-appointments
```

## Create superuser

```
make superuser
```

# If you already setup project, run

```
make run
```

## Testing our API (with CURL command-line)

```bash
# Login
http POST http://localhost:8000/api/auth/ username="admin" password="root"

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNjAxMTMzLCJpYXQiOjE3MjM2MDA4MzMsImp0aSI6IjNmMjliZGNkNjM2ZDQ5NTE4ZWU0Njk2MDQ4YzFkYTJmIiwidXNlcl9pZCI6MX0.O6Gi_YPV-jObrlfMFdQDU9KT4pKN0XwUBw_AuwoFAHg",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzY4NzIzMywiaWF0IjoxNzIzNjAwODMzLCJqdGkiOiI0MDU2NWI3ZTUxOWI0MWI3YjFlZGQ5OWEwMDAyMTFkNyIsInVzZXJfaWQiOjF9.LxjvOaOrRWtlHqP8iBTGcw7niDA1iTH12eE6WBqOWEM"
}
```

```bash
~$ curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/doctors/

```

# if you have migrations in appointments module

## migrations appointments

```

make migrations-appointments

```

`for future update Makefile`

```

make migrations MIGRATION_NAME=appointments

```

## migrate appointments

```

make migrate-appointments

```

```

make migrate MIGRATION_NAME=appointments

```

# Using HTTPIE

Get a list of doctors

```

http http://127.0.0.1:8000/api/doctors/

```

Get a snippet with `id` = 2

```

http http://127.0.0.1:8000/api/doctors/2/

```

# Postgres DB

Create DB

```

psql -U postgres

```

```

CREATE DATABASE kitboxhealth_backend_db;

```

```

CREATE USER admin WITH PASSWORD 'SXCiKvMy8#4&_W&nNT5kGX&Q2EmUKmx#nu6rDT$djdD4dHfPmnW6JFXx8dqTKhPoVfa7ZZnLmNViC4kp34UpCYg2_@YXEnqB84##fDFxmVG';

```

```

GRANT ALL PRIVILEGES ON DATABASE kitboxhealth_backend_db TO admin;

```

```

GRANT ALL PRIVILEGES ON SCHEMA public TO admin;

```

```

ALTER USER admin WITH SUPERUSER;

```

# API Documentation

Here the [Swagger Documentation](http://127.0.0.1:8000/api/doc/swagger/)

Here the [Redoc Documentation](http://127.0.0.1:8000/api/doc/redoc/)

# Deployment Essentials to Heroku

Requirements.txt: Create a file listing all your dependencies:

```

pip freeze > requirements.txt

```

Create a Procfile in your project root and add:

```

web: gunicorn kitboxhealth_backend.wsgi --log-file -

```

Runtime.txt (Optional): Specify your Python version:

```

python-3.10.14

```

```

```
