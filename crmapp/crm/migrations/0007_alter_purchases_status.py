# Generated by Django 3.2.9 on 2021-11-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_users_accesslevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved')], max_length=64),
        ),
    ]
