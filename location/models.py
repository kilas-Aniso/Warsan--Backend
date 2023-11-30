from django.db import models
class Location(models.Model):
    REGIONS_CHOICES = [
        ('Banadir', 'Banadir'),
        ('Bari', 'Bari'),
        ('Bay', 'Bay'),
        ('Galguduud', 'Galguduud'),
        ('Gedo', 'Gedo'),
        ('Hiran', 'Hiran'),
        ('Jubbada_Dhexe', 'Jubbada Dhexe'),
        ('Jubbada_Hoose', 'Jubbada Hoose'),
        ('Mudug', 'Mudug'),
        ('Nugaal', 'Nugaal'),
        ('Sanaag', 'Sanaag'),
        ('Shabeellaha_Dhexe', 'Shabeellaha Dhexe'),
        ('Shabeellaha_Hoose', 'Shabeellaha Hoose'),
        ('Sool', 'Sool'),
        ('Togdheer', 'Togdheer'),
        ('Woqooyi_Galbeed', 'Woqooyi Galbeed'),
        ('Awdal', 'Awdal'),
        ('Bakool', 'Bakool'),
        ('Lower_Juba', 'Lower Juba'),
    ]
    region = models.CharField(max_length=32, choices=REGIONS_CHOICES, default='Banadir', unique=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    def save(self, *args, **kwargs):
        default_coords = {
            'Banadir': (45.318162, 2.065367),
            'Bari': (49.821468, 10.641948),
            'Bay': (42.715303, 3.144473),
            'Galguduud': (46.250944, 5.839366),
            'Gedo': (42.571477, 3.299428),
            'Hiran': (45.548841, 4.204103),
            'Jubbada_Dhexe': (42.362506, 1.496049),
            'Jubbada_Hoose': (42.537076, 0.350559),
            'Mudug': (48.483444, 6.531853),
            'Nugaal': (49.085625, 9.213055),
            'Sanaag': (47.291020, 10.266436),
            'Shabeellaha_Dhexe': (45.838248, 2.787706),
            'Shabeellaha_Hoose': (44.287438, 1.970874),
            'Sool': (47.878628, 9.292358),
            'Togdheer': (45.557667, 9.315251),
            'Woqooyi_Galbeed': (44.072594, 9.636181),
            'Awdal': (42.258700, 9.670854),
            'Bakool': (43.120752, 6.079766),
            'Lower_Juba': (41.979833, 1.798583),
        }
        self.longitude, self.latitude = default_coords.get(self.region, (0.0, 0.0))
        super().save(*args, **kwargs)
    def __str__(self):
        return self.region
    class Meta:
        db_table = 'Location'
