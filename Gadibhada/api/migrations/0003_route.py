# Generated by Django 3.2.4 on 2021-06-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_stop_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=100)),
                ('rname', models.CharField(max_length=100)),
            ],
        ),
    ]