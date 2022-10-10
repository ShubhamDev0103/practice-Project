# Generated by Django 4.1.1 on 2022-10-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doob_app', '0005_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
