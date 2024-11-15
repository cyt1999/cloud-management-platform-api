# Generated by Django 5.1.3 on 2024-11-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=100)),
                ('domain_status', models.CharField(max_length=50)),
                ('real_name_auth_status', models.CharField(max_length=50)),
                ('registration_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
    ]