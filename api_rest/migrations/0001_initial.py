# Generated by Django 5.0.2 on 2024-03-04 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('origen', models.CharField(max_length=30)),
                ('calorias', models.IntegerField()),
                ('ingredientes', models.TextField()),
                ('disponible', models.BooleanField(default=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
