# Generated by Django 3.0.1 on 2023-04-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gittigidiyor', '0002_auto_20220402_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gittigidiyorcargomap',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gittigidiyorcargomismatch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gittigidiyorlinelog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gittigidiyorlog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gittigidiyorproductmatch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gittigidiyorproductmismatch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
