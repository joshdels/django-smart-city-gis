# Smart City GIS Offices

this is a monolith application that handles land planning offices

## Tech Stack

1. django/geodjango
2. django all auth
3. maplibre
4. postgresql / postgis
5. htmx, css, vanila js
6. s3 backblaze (cloud storage)
7. WhiteNoise
8. Vultr & Nginx

## Project Structure

```
.docker /
    │
    ├── Dockerfile
    |── docker-compose.yml

.github /
    │
    └── github/workflows
        │
        └── github/workflows


apps/
    │
    ├── accounts/        # users, roles, auth
    ├── parcels/         # GIS core (MAIN APP)
    ├── owners/          # land owners
    └── dashboard/       # UI pages, filters, map views

config/                  # users, roles, auth
templates/               # global html
static/                  # global styles and images

plans/                   # pre planing stuffs
.env                     # environment
```

## To start

### Postgres

```
sudo -u <user> psql
CREATE DATABASE <database_name>:
\c <database_name>
CREATE EXTENSION postgis
```

### Environment Structure

```
ENV=dev

SECRET_KEY="django-key"

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### Django Run Commands

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