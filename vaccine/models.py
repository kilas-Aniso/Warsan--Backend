from django.db import models

class Vaccine(models.Model):
    VACCINE_CHOICES = [
        ('BCG', 'BCG - Tuberculosis'),
        ('Polio1', 'Polio1  - OPV'),
        ('DPT-HepB-Hib1', 'DPT-HepB-Hib1 - DPT-HepB-Hib1'),
        ('DPT-HepB-Hib2', 'DPT-HepB-Hib2 - DPT-HepB-Hib2'),
        ('DPT-HepB-Hib3', 'DPT-HepB-Hib3 - DPT-HepB-Hib3'),
        ('Polio2', 'Polio2  - OPV'),
        ('PCV1', 'PCV1  - PCV1'),
        ('Rotavirus', 'Rota - Rota'),
        ('MRV1', 'Measles-Rubella Vaccine- MRV1'),
        ('PCV2', 'PCV2  - PCV'),
        ('MMR', 'Measles, Mumps, Rubella- MMR'),
        ('DPT-HepB-Hib4', 'DPT-HepB-Hib4 - DPT-HepB-Hib4'),
        ('Polio3', 'Polio3  - OPV'),
        ('HepA', 'Hepatitis A'),

    ]

    vaccine_choice = models.CharField(max_length=32, choices=VACCINE_CHOICES, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_vaccine_choice_display()