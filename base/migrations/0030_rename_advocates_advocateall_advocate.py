# Generated by Django 5.0.1 on 2024-01-07 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_advocate_company_alter_advocateall_advocates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocateall',
            old_name='advocates',
            new_name='advocate',
        ),
    ]