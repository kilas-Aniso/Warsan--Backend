from django.test import TestCase

# Create your tests here.
from .models import Vaccine

class VaccineModelTestCase(TestCase):

    def setUp(self):
        # Sample Vaccine instances for testing
        Vaccine.objects.create(
            name="DPT Dose 3",
            target_disease="Diptheria and Tetanus",
            minimum_age=8,
            maximum_age=16,
            recommended_dose=1.5
        )
        Vaccine.objects.create(
            name="Polio Dose 4",
            target_disease="Polio",
            minimum_age=5,
            maximum_age=15,
            recommended_dose=2.0
        )

    def test_vaccine_str_method(self):
        # Test the __str__ method
        vaccine1 = Vaccine.objects.get(name="DPT Dose 3")
        vaccine2 = Vaccine.objects.get(name="Polio Dose 4")
        self.assertEqual(str(vaccine1), "DPT Dose 3")
        self.assertEqual(str(vaccine2), "Polio Dose 4")

    def test_vaccine_fields(self):
        # Test the fields of the Vaccine model
        vaccine1 = Vaccine.objects.get(name="DPT Dose 3")
        vaccine2 = Vaccine.objects.get(name="Polio Dose 4")
        self.assertEqual(vaccine1.target_disease, "Diptheria and Tetanus")
        self.assertEqual(vaccine2.target_disease, "Polio")
        self.assertEqual(vaccine1.minimum_age, 8)
        self.assertEqual(vaccine2.minimum_age, 5)
        self.assertEqual(vaccine1.maximum_age, 16)
        self.assertEqual(vaccine2.maximum_age, 15)
        self.assertEqual(float(vaccine1.recommended_dose), 1.5)
        self.assertEqual(float(vaccine2.recommended_dose), 2.0)
