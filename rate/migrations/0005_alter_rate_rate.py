# Generated by Django 4.2.11 on 2024-11-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_alter_rate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.CharField(max_length=5),
        ),
    ]