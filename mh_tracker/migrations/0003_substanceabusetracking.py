# Generated by Django 4.2.11 on 2024-03-12 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mh_tracker', '0002_rename_excercise_time_journalentry_exercise_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubstanceAbuseTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('days_sober', models.IntegerField(default=0)),
                ('counter', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
