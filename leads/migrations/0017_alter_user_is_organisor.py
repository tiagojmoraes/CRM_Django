# Generated by Django 4.1.3 on 2022-12-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=False),
        ),
    ]
