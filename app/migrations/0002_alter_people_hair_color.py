# Generated by Django 4.0.3 on 2022-03-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('black,', 'Black'), ('black', 'Black')], max_length=32),
        ),
    ]
