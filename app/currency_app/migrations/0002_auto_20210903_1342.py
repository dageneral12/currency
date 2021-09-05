# Generated by Django 3.2.5 on 2021-09-03 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('source_url', models.CharField(default='', max_length=255)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now), # noqa
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
