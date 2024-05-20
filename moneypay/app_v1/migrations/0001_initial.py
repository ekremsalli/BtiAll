# Generated by Django 3.0.1 on 2021-11-16 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=64)),
                ('account', models.CharField(max_length=64)),
                ('is_debit', models.BooleanField(default=True)),
                ('formula', models.TextField(default='n')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_v1.Operation')),
            ],
        ),
    ]
