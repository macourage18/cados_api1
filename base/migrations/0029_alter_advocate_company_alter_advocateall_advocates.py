# Generated by Django 5.0.1 on 2024-01-07 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_alter_advocate_company_alter_advocateall_advocates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
        migrations.AlterField(
            model_name='advocateall',
            name='advocates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.advocate'),
        ),
    ]