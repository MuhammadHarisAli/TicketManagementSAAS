# Generated by Django 4.0.2 on 2022-02-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_types_profile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile number'),
        ),
    ]
