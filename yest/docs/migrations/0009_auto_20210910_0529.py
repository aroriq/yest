# Generated by Django 3.2.6 on 2021-09-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0008_auto_20210910_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermodel',
            name='address',
        ),
        migrations.AddField(
            model_name='customermodel',
            name='address1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='住所1'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='address2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='住所2'),
        ),
    ]
