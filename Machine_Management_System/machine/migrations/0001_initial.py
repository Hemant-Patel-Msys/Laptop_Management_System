# Generated by Django 4.2.4 on 2023-08-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Machine Name')),
                ('email', models.EmailField(max_length=277, verbose_name='Email')),
                ('comment', models.TextField(max_length=500, verbose_name='Text Area')),
            ],
        ),
    ]
