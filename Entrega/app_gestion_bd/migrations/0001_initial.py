# Generated by Django 4.1.3 on 2023-02-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
                ('matricula', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('obra_social', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
            ],
        ),
    ]
