# Generated by Django 4.2.6 on 2023-10-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experance',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='puplished_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vanancy',
            field=models.IntegerField(default=1),
        ),
    ]