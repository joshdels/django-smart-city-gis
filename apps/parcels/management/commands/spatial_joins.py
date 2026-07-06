from django.core.management.base import BaseCommand, CommandError
from django.db import connection, DatabaseError


class Command(BaseCommand):
    help = (
        "Populate spatial data such as barangay boundaries and calculate parcel area."
    )

    def handle(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:

                self.stdout.write("Assigning barangays...")

                cursor.execute("""
                    UPDATE parcels_parcel p
                    SET barangay_name = b.barangay_name
                    FROM boundaries_boundary b
                    WHERE ST_Contains(
                        b.geom,
                        ST_PointOnSurface(p.geom)
                    );
                """)

                self.stdout.write(self.style.SUCCESS("Successfully assigned barangays."))

                self.stdout.write("Calculating parcel areas...")

                cursor.execute("""
                    UPDATE parcels_parcel
                    SET area_auto_m2 = ST_Area(
                        geom::geography
                    );
                """)

                self.stdout.write(self.style.SUCCESS("Successfully caluclated Parcel areas"))

        except DatabaseError as e:
            raise CommandError(f"Database error while enriching parcels: {e}")

        except Exception as e:
            raise CommandError(f"Unexpected error: {e}")

        self.stdout.write(
            self.style.SUCCESS("Parcel enrichment completed successfully.")
        )
