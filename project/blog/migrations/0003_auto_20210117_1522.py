# Generated by Django 3.1.3 on 2021-01-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210117_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
