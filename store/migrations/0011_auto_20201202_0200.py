# Generated by Django 3.1.3 on 2020-12-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201130_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/card-thumbnail.jpg', null=True, upload_to='images'),
        ),
    ]
