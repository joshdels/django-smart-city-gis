import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Manually imports a a GIS file into PostGIS using ogr2ogr"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path", type=str, help="Absolute path to GIS file (.gpkg .shp)"
        )
        parser.add_argument("table_name", type=str, help="Target database table name")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        table_name = options["table_name"]

        db = settings.DATABASES["default"]

        pg_conn = (
            f"PG:host={db.get('HOST')} "
            f"user={db['USER']} "
            f"dbname={db['NAME']} "
            f"password={db['PASSWORD']} "
            f"port={db.get('PORT', '5432')} "
        )

        self.stdout.write(self.style.WARNING(f"Starting import of {file_path}..."))

        try:
            subprocess.run(
                [
                    "ogr2ogr",
                    "-progress",
                    "-f",
                    "PostgreSQL",
                    pg_conn,
                    file_path,
                    "-nln",
                    table_name,
                    "-append",
                    "-lco",
                    "FID=fid",
                    "-lco",
                    "GEOMETRY_NAME=geom",
                    "-nlt",
                    "PROMOTE_TO_MULTI",
                    "-t_srs",
                    "EPSG:4326",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully imported {table_name}!")
            )

        except subprocess.CalledProcessError as e:
            raise CommandError(f"ogr2ogr failed: {e.stderr}")
