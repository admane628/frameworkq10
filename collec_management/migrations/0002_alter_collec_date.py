# Generated by Django 5.1.3 on 2024-11-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collec_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collec',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
