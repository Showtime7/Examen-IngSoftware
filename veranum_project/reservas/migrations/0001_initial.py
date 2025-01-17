# Generated by Django 5.0.6 on 2024-07-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField()),
                ('hotel', models.CharField(max_length=100)),
                ('precio_noche', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('masaje', models.BooleanField(default=False)),
                ('sauna', models.BooleanField(default=False)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
