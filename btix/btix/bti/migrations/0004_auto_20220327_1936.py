# Generated by Django 3.0.1 on 2022-03-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bti', '0003_auto_20220327_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flow',
            options={'ordering': ['-id']},
        ),
    ]