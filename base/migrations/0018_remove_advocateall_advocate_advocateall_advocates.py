# Generated by Django 5.0.1 on 2024-01-06 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_advocates_advocateall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocateall',
            name='advocate',
        ),
        migrations.AddField(
            model_name='advocateall',
            name='advocates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.advocate'),
        ),
    ]
