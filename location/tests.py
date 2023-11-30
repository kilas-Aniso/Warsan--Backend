from django.test import TestCase
from .models import Location

# Create your tests here.

class LocationModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            state="Somaliland",
            region="Awdal",
            district="Borana"
        )

    def test_location_str(self):
        
        self.assertEqual(str(self.location), "Somaliland")

    def test_location_attributes(self):
       
        self.assertEqual(self.location.state, "Somaliland")
        self.assertEqual(self.location.region, "Awdal")
        self.assertEqual(self.location.district, "Borana")

    def test_location_creation(self):
       
        location_count = Location.objects.count()
        self.assertEqual(location_count, 1)

    def test_location_deletion(self):
        
        self.location.delete()
        location_count = Location.objects.count()
        self.assertEqual(location_count, 0)
