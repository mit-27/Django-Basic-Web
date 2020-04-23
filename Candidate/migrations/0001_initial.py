# Generated by Django 3.0.5 on 2020-04-23 05:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('candidate_address', models.TextField(blank=True, max_length=10, null=True)),
                ('candidate_phone', models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('candidate_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('candidate_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('candidate_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('candidate_job_title', models.CharField(choices=[('jt1', 'Developer'), ('jt2', 'Tester')], default='jt1', max_length=5)),
                ('candidate_source', models.CharField(choices=[('s1', 'Linkdln'), ('s2', 'Website')], default='s1', max_length=5)),
                ('candidate_recruiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'candidate',
                'managed': True,
            },
        ),
    ]
