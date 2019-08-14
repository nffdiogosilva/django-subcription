# Generated by Django 2.2.4 on 2019-08-13 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0010_auto_20190813_1450'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='websites', to=settings.AUTH_USER_MODEL),
        ),
    ]
