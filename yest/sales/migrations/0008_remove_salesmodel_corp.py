# Generated by Django 3.2.6 on 2021-10-08 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_salesmodel_corp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesmodel',
            name='corp',
        ),
    ]
