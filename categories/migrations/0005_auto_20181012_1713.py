# Generated by Django 2.0.6 on 2018-10-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20181009_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationcode',
            name='time',
            field=models.DurationField(default=None, null=True),
        ),
    ]
