# Generated by Django 3.0.1 on 2021-11-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bti', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('app_v1', '0002_auto_20211123_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestQueLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('exception', models.TextField(blank=True, null=True)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.Flow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestQue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
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
        ),
        migrations.CreateModel(
            name='OpQueLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('exception', models.TextField(blank=True, null=True)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.Flow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpQue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(db_index=True, default=False)),
                ('is_cancelled', models.BooleanField(db_index=True, default=False)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('day', models.DateField(db_index=True)),
                ('op', models.CharField(db_index=True, max_length=64)),
            ],
            options={
                'abstract': False,
                'unique_together': {('firm', 'identifier')},
            },
        ),
        migrations.CreateModel(
            name='InvoiceQueLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('exception', models.TextField(blank=True, null=True)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.Flow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceQue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(db_index=True, default=False)),
                ('is_cancelled', models.BooleanField(db_index=True, default=False)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('day', models.DateField(db_index=True)),
            ],
            options={
                'abstract': False,
                'unique_together': {('firm', 'identifier')},
            },
        ),
    ]
