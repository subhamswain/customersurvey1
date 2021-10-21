# Generated by Django 3.2.8 on 2021-10-20 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customersurvey', '0002_survey_survey_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='user_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='tbl_questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='survey',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customersurvey.tbl_questions'),
        ),
    ]
