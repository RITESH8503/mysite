# Generated by Django 4.0.3 on 2022-04-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contact',
            field=models.IntegerField(default='+91'),
        ),
    ]
