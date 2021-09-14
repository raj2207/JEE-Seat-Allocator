# Generated by Django 3.0.4 on 2020-03-23 08:18

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0002_auto_20200323_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default='a@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='preferences',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
