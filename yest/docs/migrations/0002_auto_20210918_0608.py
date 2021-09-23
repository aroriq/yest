# Generated by Django 3.2.6 on 2021-09-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmodel',
            name='jsdate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='重説実施日'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='zanmuremarks',
            field=models.TextField(blank=True, default='', null=True, verbose_name='残務処理特記事項'),
        ),
    ]