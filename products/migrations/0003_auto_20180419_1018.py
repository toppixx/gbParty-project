# Generated by Django 2.0.4 on 2018-04-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180418_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supporter',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='hunter',
            field=models.TextField(),
        ),
    ]
