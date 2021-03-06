# Generated by Django 2.2.4 on 2020-05-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantLogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(default='cuisine', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='first_name',
            field=models.CharField(default='fname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='last_name',
            field=models.CharField(default='lname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(default=123456789, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='email_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='password',
            field=models.CharField(max_length=70),
        ),
    ]
