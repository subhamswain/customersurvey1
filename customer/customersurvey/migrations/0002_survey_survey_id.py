# Generated by Django 3.2.8 on 2021-10-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customersurvey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='survey_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
