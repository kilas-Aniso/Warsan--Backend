from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType  
from .models import CustomUser, Healthworker
from faker import Faker

class ModelTestCase(TestCase):
    def setUp(self):
        fake = Faker()

        # Create a Group
        self.group = Group.objects.create(name='Test Group')

        # Create a ContentType
        content_type = ContentType.objects.create(
            app_label='registration',  
            model='Custom User', 
        )

        # Create a Permission
        self.permission = Permission.objects.create(
            codename='test_permission',
            name='Test Permission',
            content_type=content_type,  
        )

        # Create a CustomUser
        self.custom_user = CustomUser.objects.create(
            username=fake.user_name(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        self.custom_user.groups.add(self.group)
        self.custom_user.user_permissions.add(self.permission)

        # Create a Healthworker
        self.healthworker = Healthworker.objects.create(
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number=fake.phone_number(),
            location=fake.city(),
            created_by=self.custom_user,
        )
        self.healthworker.groups.add(self.group)
        self.healthworker.user_permissions.add(self.permission)

    def test_custom_user_creation(self):
        custom_user = CustomUser.objects.get(username=self.custom_user.username)
        print("Custom User:")
        print("Username:", custom_user.username)
        print("Email:", custom_user.email)
        print("First Name:", custom_user.first_name)
        print("Last Name:", custom_user.last_name)
        self.assertEqual(custom_user.email, self.custom_user.email)
        self.assertEqual(custom_user.first_name, self.custom_user.first_name)
        self.assertEqual(custom_user.last_name, self.custom_user.last_name)
        self.assertTrue(custom_user.groups.filter(name='Test Group').exists())
        self.assertTrue(custom_user.user_permissions.filter(codename='test_permission').exists())

    def test_healthworker_creation(self):
        healthworker = Healthworker.objects.get(username=self.healthworker.username)
        print("Healthworker:")
        print("Username:", healthworker.username)
        print("First Name:", healthworker.first_name)
        print("Last Name:", healthworker.last_name)
        print("Phone Number:", healthworker.phone_number)
        print("Location:", healthworker.location)
        print("Created By:", healthworker.created_by)
        self.assertEqual(healthworker.first_name, self.healthworker.first_name)
        self.assertEqual(healthworker.last_name, self.healthworker.last_name)
        self.assertEqual(healthworker.phone_number, self.healthworker.phone_number)
        self.assertEqual(healthworker.location, self.healthworker.location)
        self.assertEqual(healthworker.created_by, self.custom_user)
        self.assertTrue(healthworker.groups.filter(name='Test Group').exists())
        self.assertTrue(healthworker.user_permissions.filter(codename='test_permission').exists())
