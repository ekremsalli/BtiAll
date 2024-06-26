# Generated by Django 3.2.12 on 2023-03-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robotpos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rotated', models.BooleanField(db_index=True, default=False, verbose_name='Dosyaya yönlendirildi')),
                ('rotated_to', models.TextField(blank=True, null=True, verbose_name='Yönlendirilen dosya')),
                ('rotated_at', models.DateTimeField(blank=True, null=True, verbose_name='Yönlendirilme zamanı')),
                ('rotated_fields', models.CharField(blank=True, max_length=255, null=True)),
                ('day', models.DateField(db_index=True)),
                ('genre', models.CharField(choices=[('branch_revenue', 'branch_revenue'), ('sales', 'sales'), ('pcw', 'pcw'), ('sales_invoice', 'sales_invoice'), ('accounting', 'accounting'), ('wantage', 'wantage'), ('refund', 'refund')], db_index=True, max_length=32)),
                ('branch', models.IntegerField(db_index=True)),
                ('data', models.TextField()),
                ('is_empty', models.BooleanField(db_index=True, default=True)),
                ('is_error', models.BooleanField(db_index=True, default=False)),
                ('is_accounted', models.BooleanField(db_index=True, default=False)),
                ('last_error', models.TextField(null=True)),
                ('last_synced', models.DateField(null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'unique_together': {('day', 'genre', 'branch')},
            },
        ),
    ]
