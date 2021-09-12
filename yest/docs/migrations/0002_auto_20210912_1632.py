# Generated by Django 3.2.6 on 2021-09-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmodel',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='住所1'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='住所2'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default='', null=True, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='birthday',
            field=models.CharField(blank=True, default='年月日', max_length=20, null=True, verbose_name='生年月日'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='department',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='部署'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='fax',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='FAX'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', '男性'), ('2', '女性'), ('3', 'その他')], default='', max_length=1, null=True, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='remarks',
            field=models.TextField(blank=True, default='特記なし', null=True, verbose_name='特記事項'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='tel1',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='電話番号1'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='tel2',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='電話番号2'),
        ),
    ]
