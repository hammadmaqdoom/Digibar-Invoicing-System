# Generated by Django 3.2.9 on 2021-11-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_business_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='accessLevel',
            field=models.CharField(choices=[('admin', 'Admin'), ('business', 'Business'), ('compuser', 'CompanyUser')], max_length=50),
        ),
    ]
