# Generated by Django 2.0.2 on 2018-03-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_site',
            new_name='profile_site',
        ),
    ]