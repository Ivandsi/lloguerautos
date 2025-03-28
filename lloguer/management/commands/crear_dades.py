import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from lloguer.models import Automobil, Reserva  # Replace 'app' with your actual app name

fake = Faker()

class Command(BaseCommand):
    help = "Creates new users, automobiles, and reservations without deleting existing data."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🔹 Generating new data..."))

        # Create 4 new automobiles
        automobils = []
        for _ in range(4):
            automobil = Automobil.objects.create(
                marca=fake.company(),
                model=fake.word().capitalize(),
                matricula=fake.unique.license_plate()
            )
            automobils.append(automobil)

        self.stdout.write(self.style.SUCCESS("✔ 4 New Automobiles Created!"))

        # Create 8 new users with unique usernames (retry up to 3 times if taken)
        existing_usernames = set(User.objects.values_list('username', flat=True))
        new_users = []

        for _ in range(8):
            attempts = 0
            new_username = None

            while attempts < 3:
                new_username = fake.user_name()
                if new_username not in existing_usernames:
                    break
                attempts += 1  # Try again if it's taken

            if new_username and new_username not in existing_usernames:
                user = User.objects.create_user(username=new_username, password="password")
                new_users.append(user)
                existing_usernames.add(new_username)

        self.stdout.write(self.style.SUCCESS("✔ 8 New Unique Users Created!"))

        # Assign 1 or 2 new reservations per user
        for user in new_users:
            num_reserves = random.randint(1, 2)
            for _ in range(num_reserves):
                data_inici = now() + timedelta(days=random.randint(1, 30))
                data_fi = data_inici + timedelta(days=random.randint(1, 7))
                automobil = random.choice(automobils)

                Reserva.objects.create(
                    user=user,
                    automobil=automobil,
                    data_inici=data_inici,
                    data_fi=data_fi
                )

        self.stdout.write(self.style.SUCCESS("✔ New Reservations Created!"))
        self.stdout.write(self.style.SUCCESS("✅ Seeder Completed Successfully!"))
