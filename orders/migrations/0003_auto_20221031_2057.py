# Generated by Django 3.0.3 on 2022-10-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='style',
            field=models.CharField(choices=[('R', 'Regular'), ('D', 'Dinosaur')], max_length=1),
        ),
    ]
