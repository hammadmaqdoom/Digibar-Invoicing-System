# Generated by Django 3.2.9 on 2021-11-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_item_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='itemID',
        ),
        migrations.AddField(
            model_name='sales',
            name='items',
            field=models.ManyToManyField(to='crm.ProductsAndServices'),
        ),
        migrations.DeleteModel(
            name='Item_sale',
        ),
    ]
