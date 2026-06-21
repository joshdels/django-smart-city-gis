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

prerequisite (start a postgres)
```
sudo -u <user> psql
CREATE DATABASE <database_name>:
\c <database_name>
CREATE EXTENSIONS postgis

```


```
uv sync
python manage.py migrate
python manage.py runserver
```