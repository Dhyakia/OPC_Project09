# Generated by Django 4.0.3 on 2022-04-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_userfollows'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
