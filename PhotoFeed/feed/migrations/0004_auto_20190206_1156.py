# Generated by Django 2.1.5 on 2019-02-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20190206_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
