# Generated by Django 3.2.6 on 2023-11-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_alter_vaccine_vaccine_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_choice',
            field=models.CharField(choices=[('BCG', 'BCG - Tuberculosis'), ('Polio1', 'Polio1  - OPV'), ('DPT-HepB-Hib1', 'DPT-HepB-Hib1 - DPT-HepB-Hib1'), ('DPT-HepB-Hib2', 'DPT-HepB-Hib2 - DPT-HepB-Hib2'), ('DPT-HepB-Hib3', 'DPT-HepB-Hib3 - DPT-HepB-Hib3'), ('Polio2', 'Polio2  - OPV'), ('PCV1', 'PCV1  - PCV1'), ('Rotavirus', 'Rota - Rota'), ('MRV1', 'Measles-Rubella Vaccine- MRV1'), ('PCV2', 'PCV2  - PCV'), ('MMR', 'Measles, Mumps, Rubella- MMR'), ('DPT-HepB-Hib4', 'DPT-HepB-Hib4 - DPT-HepB-Hib4'), ('Polio3', 'Polio3  - OPV'), ('HepA', 'Hepatitis A')], max_length=32, null=True, unique=True),
        ),
    ]
