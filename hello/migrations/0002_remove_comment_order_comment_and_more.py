# Generated by Django 4.2.3 on 2023-07-08 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='order_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='sight_comment',
        ),
        migrations.DeleteModel(
            name='OrderComment',
        ),
        migrations.DeleteModel(
            name='SightComment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Sight',
        ),
    ]