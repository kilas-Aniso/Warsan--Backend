# Generated by Django 3.2.6 on 2023-10-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_choice', models.CharField(choices=[('BCG', 'BCG - Tuberculosis'), ('HepB', 'Hepatitis B'), ('DTP', 'DTP - Diphtheria, Tetanus, Pertussis'), ('IPV', 'IPV  - Polio'), ('HiB', 'HiB - Haemophilus influenzae type b'), ('PCV13', 'PCV13- Pneumococcal disease'), ('RV', 'RV - Rotavirus'), ('MMR', 'MMR- Measles, Mumps, Rubella'), ('Varicella', 'Varicella - Chickenpox'), ('HepA', 'Hepatitis A'), ('MenACWY', 'MenACWY- Meningococcal disease'), ('DTaP-IPV-HiB-HepB', 'DTaP-IPV-HiB-HepB - Diphtheria, Tetanus, Pertussis, Polio, Haemophilus influenzae type b, Hepatitis B'), ('Influenza', 'Influenza (Seasonal)')], max_length=32, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]