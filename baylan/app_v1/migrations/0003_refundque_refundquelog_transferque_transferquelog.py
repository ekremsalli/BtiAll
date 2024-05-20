# Generated by Django 3.2.12 on 2022-12-28 15:35

import app_v1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bti', '0005_auto_20220402_2353'),
        ('app_v1', '0002_expanseque_expansequelog_purchasedispatchque_purchasedispatchquelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferQueLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('exception', models.TextField(blank=True, null=True)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.flow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransferQue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_processing', models.BooleanField(db_index=True, default=False)),
                ('is_processed', models.BooleanField(db_index=True, default=False)),
                ('is_cancelled', models.BooleanField(db_index=True, default=False)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
                'unique_together': {('firm', 'identifier')},
            },
            bases=(models.Model, app_v1.models.CommonQue),
        ),
        migrations.CreateModel(
            name='RefundQueLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('exception', models.TextField(blank=True, null=True)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.flow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RefundQue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_processing', models.BooleanField(db_index=True, default=False)),
                ('is_processed', models.BooleanField(db_index=True, default=False)),
                ('is_cancelled', models.BooleanField(db_index=True, default=False)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
                'unique_together': {('firm', 'identifier')},
            },
            bases=(models.Model, app_v1.models.CommonQue),
        ),
    ]
