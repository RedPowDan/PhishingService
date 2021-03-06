# Generated by Django 3.2.10 on 2021-12-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generators', '0002_auto_20211231_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='referenceinfo',
            name='count_views',
            field=models.BooleanField(default=0, verbose_name='Кол-во просмотров страницы'),
        ),
        migrations.AddField(
            model_name='referenceinfo',
            name='is_post_data',
            field=models.BooleanField(default=False, verbose_name='Отправил ли информацию котрая указана в форме'),
        ),
    ]
