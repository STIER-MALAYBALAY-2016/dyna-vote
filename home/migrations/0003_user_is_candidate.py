# Generated by Django 3.1.6 on 2021-02-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210210_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_candidate',
            field=models.BooleanField(default=False),
        ),
    ]
