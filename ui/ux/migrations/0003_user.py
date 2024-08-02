# Generated by Django 5.0.6 on 2024-08-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ux', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
    ]
