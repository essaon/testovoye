# Generated by Django 4.2.5 on 2023-10-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0003_remove_menuitem_named_url_remove_menuitem_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
