# Generated by Django 4.0.4 on 2022-06-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogname', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
            ],
        ),
    ]
