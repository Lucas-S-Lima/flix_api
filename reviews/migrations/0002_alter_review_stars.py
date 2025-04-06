# Generated by Django 5.1.6 on 2025-03-14 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Apenas avaliações maiores que 0 e menores ou iguais a 5.'), django.core.validators.MaxValueValidator(5, 'Apenas avaliações maiores que 0 e menores ou iguais a 5.')]),
        ),
    ]
