# Generated by Django 3.2.9 on 2021-11-11 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20211111_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsandservices',
            name='psName',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
    ]