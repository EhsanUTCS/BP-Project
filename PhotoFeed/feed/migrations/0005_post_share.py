# Generated by Django 2.1.5 on 2019-02-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20190206_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='share',
            field=models.BooleanField(default=False),
        ),
    ]
