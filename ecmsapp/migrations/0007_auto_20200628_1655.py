# Generated by Django 3.0.3 on 2020-06-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecmsapp', '0006_shop_shop_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile2.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_picture',
            field=models.ImageField(blank=True, default='shop.jpg', null=True, upload_to=''),
        ),
    ]
