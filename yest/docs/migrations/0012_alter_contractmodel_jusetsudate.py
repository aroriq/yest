# Generated by Django 3.2.6 on 2021-09-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0011_auto_20210917_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='jusetsudate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='重説実施日'),
        ),
    ]
