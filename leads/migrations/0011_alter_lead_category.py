# Generated by Django 4.1.3 on 2022-12-22 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_alter_category_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='leads.category'),
        ),
    ]
