# Generated by Django 4.0.1 on 2022-11-12 21:34

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='arguments',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]
