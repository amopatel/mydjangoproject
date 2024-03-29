# Generated by Django 2.2.6 on 2019-11-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Home Appliance', 'Home Appliance')], default='', max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_brand', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_price', models.CharField(max_length=10)),
                ('product_desc', models.TextField()),
            ],
        ),
    ]
