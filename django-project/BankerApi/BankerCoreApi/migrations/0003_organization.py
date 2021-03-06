# Generated by Django 2.2 on 2019-05-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankerCoreApi', '0002_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganizationID', models.CharField(max_length=255)),
                ('OrganizationName', models.CharField(max_length=255)),
                ('OrganizationNameLowercase', models.CharField(max_length=255)),
                ('ZipCode', models.CharField(max_length=255)),
                ('DateCreated', models.CharField(max_length=255)),
                ('DateVerified', models.CharField(max_length=255)),
                ('IsActive', models.CharField(max_length=255)),
                ('IsCreatorVerified', models.CharField(max_length=255)),
                ('CreatorEmail', models.CharField(max_length=255)),
                ('CreatorWebID', models.CharField(max_length=255)),
            ],
        ),
    ]
