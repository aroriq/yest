# Generated by Django 3.2.6 on 2021-09-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0009_auto_20210919_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractmodel',
            name='kanriremarks',
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='receiptremarks1',
            field=models.TextField(blank=True, default='', null=True, verbose_name='領収書\u3000備考'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='receiptremarks2',
            field=models.TextField(blank=True, default='', null=True, verbose_name='預り証\u3000備考'),
        ),
        migrations.AlterField(
            model_name='contractmodel',
            name='kanridoc',
            field=models.TextField(blank=True, default='拝啓\u3000時下益々ご清栄のこととお慶び申し上げます。\n\nいつもお世話になっております。\n\n表記物件の入居申込書を送付致します。\n\n（送信枚数\u3000本紙を含め\u3000\u3000枚）\n\n【備考】\n\n', null=True, verbose_name='管理会社宛FAX\u3000本文'),
        ),
        migrations.AlterField(
            model_name='contractmodel',
            name='transdate',
            field=models.TextField(blank=True, default='第1希望 月\u3000日\u3000:  ～\u3000: \n\n第2希望 月\u3000日\u3000:  ～\u3000: \n\n第3希望 月\u3000日\u3000:  ～\u3000: ', null=True, verbose_name='引越連絡希望日'),
        ),
    ]
