# Generated by Django 3.1.2 on 2021-01-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='item',
            new_name='description',
        ),
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]