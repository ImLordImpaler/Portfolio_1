# Generated by Django 4.2.7 on 2023-11-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_alter_work_desc_alter_work_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email_id',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
