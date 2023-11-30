from django.test import TestCase
from rest_framework.test import APIClient
from child.models import Child, Guardian
from faker import Faker

class ChildModelTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()

        self.guardian = Guardian.objects.create(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            location=self.faker.city(),
            phone_number=self.faker.phone_number()
        )
        self.child = Child.objects.create(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            date_of_birth=self.faker.date_of_birth(minimum_age=1, maximum_age=18),
            gender=self.faker.random_element(elements=('M', 'F')),
            guardian=self.guardian
        )

    def test_child_creation(self):
        self.assertEqual(str(self.child), f"{self.child.first_name} {self.child.last_name} (Child of {self.guardian.first_name} {self.guardian.last_name})")

class GuardianModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faker = Faker()

        self.guardian_data = {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'location': self.faker.city(),
            'phone_number': self.faker.phone_number()
        }
        self.guardian = Guardian.objects.create(**self.guardian_data)

    def test_guardian_creation(self):
        self.assertEqual(str(self.guardian), f"{self.guardian.first_name} {self.guardian.last_name}")

    def test_register_child(self):
        child_data = {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'date_of_birth': self.faker.date_of_birth(minimum_age=1, maximum_age=18),
            'gender': self.faker.random_element(elements=('M', 'F')),
            'guardian': self.guardian.id
        }

        response = self.client.post('/api/children/', child_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_children(self):
        child1 = Child.objects.create(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            date_of_birth=self.faker.date_of_birth(minimum_age=1, maximum_age=18),
            gender=self.faker.random_element(elements=('M', 'F')),
            guardian=self.guardian
        )
        child2 = Child.objects.create(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            date_of_birth=self.faker.date_of_birth(minimum_age=1, maximum_age=18),
            gender=self.faker.random_element(elements=('M', 'F')),
            guardian=self.guardian
        )
        children = self.guardian.children.all()
        self.assertEqual(children.count(), 2)
