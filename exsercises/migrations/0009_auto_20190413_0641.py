# Generated by Django 2.0.6 on 2019-04-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exsercises', '0008_auto_20190331_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='choseanswerexsercise',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listenandreadexsercise',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rewritesentenceexsercise',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatesentenceexsercise',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
    ]
