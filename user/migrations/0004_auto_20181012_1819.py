# Generated by Django 2.0.6 on 2018-10-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181012_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
