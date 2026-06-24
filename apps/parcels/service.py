import subprocess
from django.conf import settings


def import_shapefile(shp_path, table_name):

    db = settings.DATABASES["default"]

    pg_conn = (
        f"PG:host={db['HOST']} "
        f"user={db['USER']} "
        f"dbname={db['NAME']} "
        f"password={db['PASSWORD']}"
        f"port={db['PORT']} "
    )

    subprocess.run(
        [
            "ogr2ogr",
            "-f",
            "PostgreSQL",
            pg_conn,
            shp_path,
            "-nln",
            table_name,
            "-overwrite",
            "-lco",
            "GEOMETRY_NAME=geom",
            "-lco",
            "FID=id",
            "-nlt",
            "PROMOTE_TO_MULTI",
        ],
        check=True,
    )
