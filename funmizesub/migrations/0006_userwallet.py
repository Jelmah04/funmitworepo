# Generated by Django 3.1.5 on 2021-03-07 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funmizesub', '0005_delete_transaction_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('walletID', models.CharField(default='', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserWallet',
                'verbose_name_plural': 'UserWallets',
                'db_table': 'UserWallet',
                'managed': True,
            },
        ),
    ]
