# Generated by Django 4.0.3 on 2022-03-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_people_hair_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(choices=[('black,', 'Black'), ('brown', 'Brown')], max_length=32),
        ),
    ]