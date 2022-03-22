# Generated by Django 4.0.1 on 2022-03-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'Settings'},
        ),
        migrations.AddField(
            model_name='settings',
            name='host',
            field=models.CharField(choices=[('smtp.gmail.com', 'gmail'), ('smtp-mail.outlook.com', 'outlook')], default='smtp.gmail.com', max_length=255),
        ),
        migrations.AlterField(
            model_name='settings',
            name='port',
            field=models.PositiveIntegerField(choices=[(587, 'gmail'), (587, 'outlook')], default=587),
        ),
        migrations.AlterField(
            model_name='settings',
            name='to_email',
            field=models.EmailField(max_length=254),
        ),
    ]