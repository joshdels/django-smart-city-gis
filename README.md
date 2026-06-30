# Smart City GIS Offices

this is a monolith application that handles planning offices

## Tech Stack

1. django/geodjango
2. django all auth
3. maplibre
4. postgresql / postgis
5. htmx and vanila js

## Project Structure

```
apps/
│
├── accounts/        # users, roles, auth
├── parcels/         # GIS core (MAIN APP)
├── owners/          # land owners
└── dashboard/       # UI pages, filters, map views

config/              # users, roles, auth

manage.py

plans/               # pre planing stuffs
.env                 # environment
```

## To start

### postgres

```
sudo -u <user> psql
CREATE DATABASE <database_name>:
\c <database_name>
CREATE EXTENSION postgis
```

### .env structure

```
ENV=dev

SECRET_KEY="django-key"

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### run django server

```
uv sync
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

to ingest gis files
```
python manage.py import_gis <shapefile path> <table_name>
```