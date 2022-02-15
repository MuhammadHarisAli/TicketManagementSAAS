# Generated by Django 4.0.2 on 2022-02-15 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_adminrequesterapprovalhirearchy'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequesterApprovalState',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='general.base')),
                ('request_approved', models.BooleanField(default=False, verbose_name='Request Approved')),
                ('hirearchy_position', models.CharField(blank=True, max_length=100, null=True)),
                ('approval_hirearchy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.adminrequesterapprovalhirearchy')),
                ('requester_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to='general.requester')),
            ],
            bases=('general.base',),
        ),
    ]