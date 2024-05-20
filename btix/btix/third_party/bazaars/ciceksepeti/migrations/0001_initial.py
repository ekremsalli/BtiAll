# Generated by Django 3.0.1 on 2022-03-25 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiceksepetiCargoMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_val', models.CharField(db_index=True, max_length=150)),
                ('output_val', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'btix_ciceksepeti_cargo_map',
            },
        ),
        migrations.CreateModel(
            name='CiceksepetiCargoMismatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(db_index=True, max_length=255, unique=True)),
                ('input_val', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'btix_ciceksepeti_cargo_mismatch',
            },
        ),
        migrations.CreateModel(
            name='CiceksepetiLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('order_number', models.CharField(db_index=True, max_length=255, unique=True)),
                ('order_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('raw', models.TextField()),
                ('internal_ref', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'btix_ciceksepeti_log',
            },
        ),
        migrations.CreateModel(
            name='CiceksepetiProductMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erp_code', models.CharField(db_index=True, max_length=100)),
                ('barcode', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('product_code', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('merchant_sku', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'btix_ciceksepeti_product_match',
            },
        ),
        migrations.CreateModel(
            name='CiceksepetiProductMismatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(db_index=True, max_length=255, unique=True)),
                ('barcode', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('product_code', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('merchant_sku', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('line', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'btix_ciceksepeti_product_mismatch',
            },
        ),
        migrations.CreateModel(
            name='CiceksepetiLineLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('line', models.CharField(db_index=True, max_length=255)),
                ('raw', models.TextField()),
                ('internal_ref', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciceksepeti.CiceksepetiLog')),
            ],
            options={
                'db_table': 'btix_ciceksepeti_line_log',
            },
        ),
    ]
