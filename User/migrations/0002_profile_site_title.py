# Generated by Django 4.0.1 on 2022-02-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='site_title',
            field=models.CharField(default='Idenify', max_length=10),
        ),
    ]