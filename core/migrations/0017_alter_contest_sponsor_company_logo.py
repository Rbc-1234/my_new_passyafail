# Generated by Django 4.0.1 on 2022-03-07 12:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_contest_sponsor_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest_sponsor',
            name='company_logo',
            field=models.FileField(blank=True, default=None, error_messages={'unique': 'only jpg format supported!'}, null=True, upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['jpg'])]),
        ),
    ]
