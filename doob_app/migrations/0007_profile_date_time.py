# Generated by Django 4.1.1 on 2022-10-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doob_app', '0006_profile_address_alter_profile_profile_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_time',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
