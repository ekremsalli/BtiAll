# Generated by Django 3.2.12 on 2022-04-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bti', '0004_auto_20220327_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='taskactivity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
