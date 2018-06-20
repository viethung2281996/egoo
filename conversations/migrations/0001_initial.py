# Generated by Django 2.0.6 on 2018-06-19 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
                ('image', models.TextField()),
                ('audio', models.TextField()),
                ('order', models.IntegerField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.Unit')),
            ],
        ),
    ]
