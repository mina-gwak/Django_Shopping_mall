# Generated by Django 3.1.3 on 2020-11-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='registered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
