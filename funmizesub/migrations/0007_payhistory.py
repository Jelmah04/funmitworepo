# Generated by Django 3.1.5 on 2021-03-12 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funmizesub', '0006_userwallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paystack_charge_id', models.CharField(blank=True, default='', max_length=100)),
                ('paystack_access_code', models.CharField(blank=True, default='', max_length=100)),
                ('payment_for', models.CharField(default='wallet funding', max_length=70, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]