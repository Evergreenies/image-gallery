# Generated by Django 2.0 on 2018-08-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary1', '0002_auto_20180810_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(max_length=300, upload_to=''),
        ),
    ]