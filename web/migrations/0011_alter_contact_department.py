# Generated by Django 4.2.3 on 2023-08-16 09:56

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [('web', '0010_remove_contact_last_name_remove_contact_website')]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='department',
            field=models.CharField(
                choices=[('', 'Services'), ('finance', 'Finance'), ('investment', 'Investment'), ('others', 'Others')],
                max_length=50,
            ),
        )
    ]
