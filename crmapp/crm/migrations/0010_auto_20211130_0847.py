# Generated by Django 3.2.9 on 2021-11-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20211129_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='itemID',
        ),
        migrations.AddField(
            model_name='purchases',
            name='items',
            field=models.ManyToManyField(to='crm.ProductsAndServices'),
        ),
    ]
