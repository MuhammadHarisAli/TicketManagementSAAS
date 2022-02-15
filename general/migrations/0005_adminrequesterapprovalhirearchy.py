# Generated by Django 4.0.2 on 2022-02-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_alter_requester_deactivation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRequesterApprovalHirearchy',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='general.base')),
                ('department_hirearchy_position', models.CharField(blank=True, max_length=100, null=True)),
                ('department_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to='general.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('general.base',),
        ),
    ]