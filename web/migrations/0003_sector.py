# Generated by Django 4.2.3 on 2023-08-01 05:40

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [('web', '0002_alter_contact_department')]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('summary', models.CharField(max_length=335)),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='image')),
            ],
        )
    ]
