# Generated by Django 3.2.6 on 2021-09-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_auto_20210910_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='contractInfo',
            field=models.CharField(default='物件名等', max_length=100, verbose_name='契約情報'),
        ),
    ]