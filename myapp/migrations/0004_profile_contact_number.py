# Generated by Django 4.2.5 on 2023-10-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
