# Generated by Django 4.2.3 on 2023-07-08 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=64, verbose_name='订单号')),
                ('amount', models.FloatField(verbose_name='订单金额')),
            ],
        ),
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('score', models.FloatField(default=5, verbose_name='评分')),
            ],
        ),
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='景点名称')),
                ('address', models.CharField(max_length=256, verbose_name='景点地址')),
            ],
        ),
        migrations.CreateModel(
            name='SightComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('score', models.FloatField(default=5, verbose_name='评分')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('score', models.FloatField(default=5, verbose_name='评分')),
                ('order_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.order')),
                ('sight_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.sight')),
            ],
        ),
    ]
