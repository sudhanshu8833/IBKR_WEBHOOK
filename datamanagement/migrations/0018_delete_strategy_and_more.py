# Generated by Django 4.2.7 on 2023-11-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0017_admin_angel_api_keys_admin_angel_client_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='strategy',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='angel_client_id',
            new_name='oanda_account_id',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='angel_api_keys',
            new_name='oanda_api_keys',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='angel_password',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='angel_token',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='admin',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='admin',
            name='stoploss_pips',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='admin',
            name='symbol',
            field=models.CharField(default='SPX500_USD', max_length=20),
        ),
    ]