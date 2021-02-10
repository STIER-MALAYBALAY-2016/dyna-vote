# Generated by Django 3.1.6 on 2021-02-10 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210210_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidacy', to=settings.AUTH_USER_MODEL),
        ),
    ]
