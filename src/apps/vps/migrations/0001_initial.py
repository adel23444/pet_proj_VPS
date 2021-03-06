# Generated by Django 4.0.2 on 2022-02-04 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('uid', models.IntegerField(db_column='UID', help_text='UID', primary_key=True, serialize=False, verbose_name='UID')),
                ('cpu', models.IntegerField(db_column='CPU', help_text='Ядра CPU', verbose_name='Ядра CPU')),
                ('ram', models.IntegerField(db_column='RAM', help_text='Объем RAM (в ГБ)', verbose_name='Объем RAM (в ГБ)')),
                ('hdd', models.IntegerField(db_column='HDD', help_text='Объем HDD (в ТБ)', verbose_name='Объем HDD (в ТБ)')),
                ('status', models.IntegerField(choices=[(1, 'started'), (0, 'stopped'), (-1, 'blocked')], db_column='status', help_text='Статус', verbose_name='Статус')),
            ],
        ),
    ]
