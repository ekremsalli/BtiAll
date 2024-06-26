# Generated by Django 3.2.12 on 2023-03-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotpos', '0002_alter_robotpos_last_synced'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentBlacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(db_index=True, max_length=10, null=True)),
                ('payment', models.CharField(db_index=True, max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(db_index=True, max_length=10, null=True)),
                ('payment', models.CharField(db_index=True, max_length=50)),
                ('account_code', models.CharField(max_length=50, null=True)),
                ('custom_field1', models.CharField(max_length=50, null=True)),
                ('custom_field2', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='robotpos',
            name='branch',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.CreateModel(
            name='PaymentError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(db_index=True, max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('branch', 'name')},
            },
        ),
    ]
