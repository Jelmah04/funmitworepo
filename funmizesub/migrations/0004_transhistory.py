# Generated by Django 3.1.5 on 2021-03-04 12:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funmizesub', '0003_transaction_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=50)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('reference_id', models.CharField(max_length=50)),
                ('status', models.CharField(default='Success', max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('prebal', models.IntegerField(blank=True, null=True)),
                ('postbal', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transhistory',
                'verbose_name_plural': 'Transhistorys',
                'db_table': 'Transhistory',
                'managed': True,
            },
        ),
    ]