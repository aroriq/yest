# Generated by Django 3.2.6 on 2021-09-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_auto_20210918_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmodel',
            name='kanridoc',
            field=models.TextField(blank=True, default='', null=True, verbose_name='契約費明細書\u3000提出書類'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='kanriremarks',
            field=models.TextField(blank=True, default='', null=True, verbose_name='引越見積依頼書\u3000備考'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='key1',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='鍵本数(部屋)'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='key2',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='鍵本数(車庫)'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='key3',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='鍵本数(トランクルーム)'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='reportdoc',
            field=models.TextField(blank=True, default='', null=True, verbose_name='契約関係書類報告書\u3000添付書類'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='reportremarks',
            field=models.TextField(blank=True, default='', null=True, verbose_name='契約関係書類報告書\u3000備考'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='transdate',
            field=models.TextField(blank=True, default='第1希望 月\u3000日\u3000:  ～\u3000: ', null=True, verbose_name='引越連絡希望日'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='transremarks',
            field=models.TextField(blank=True, default='', null=True, verbose_name='引越見積依頼書\u3000備考'),
        ),
    ]
