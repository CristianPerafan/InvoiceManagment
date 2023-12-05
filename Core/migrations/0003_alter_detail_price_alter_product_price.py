# Generated by Django 5.0 on 2023-12-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_detail_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]