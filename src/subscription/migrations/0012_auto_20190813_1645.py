# Generated by Django 2.2.4 on 2019-08-13 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0011_auto_20190813_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='subscription',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscription.Plan'),
        ),
    ]
