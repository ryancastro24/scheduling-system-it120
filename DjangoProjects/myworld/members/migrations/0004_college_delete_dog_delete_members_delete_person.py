# Generated by Django 4.0.4 on 2022-06-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('numberOfUnits', models.CharField(max_length=200)),
                ('timeAndDate', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='dog',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]
