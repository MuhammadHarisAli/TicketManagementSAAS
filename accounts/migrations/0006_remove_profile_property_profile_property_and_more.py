# Generated by Django 4.0.2 on 2022-02-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_requester'),
        ('accounts', '0005_profile_admin_profile_department_profile_employee_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='property',
        ),
        migrations.AddField(
            model_name='profile',
            name='property',
            field=models.ManyToManyField(blank=True, null=True, to='general.Property'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.SmallIntegerField(choices=[(1, 'Super Admin'), (2, 'Admin'), (3, 'User'), (4, 'Requester')], default=1, verbose_name='User type'),
        ),
    ]
