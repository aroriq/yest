# Generated by Django 3.2.6 on 2021-09-18 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmodel',
            name='sum',
            field=models.PositiveSmallIntegerField(blank=True, default=None, editable=False, null=True, verbose_name='合計金額(税込)'),
        ),
    ]
