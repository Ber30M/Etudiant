# Generated by Django 4.1 on 2022-08-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=26)),
                ('prenom', models.CharField(max_length=26)),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=10)),
                ('date_naissance', models.DateField()),
                ('fac', models.CharField(max_length=40)),
            ],
        ),
    ]
