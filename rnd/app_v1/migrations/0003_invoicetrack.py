# Generated by Django 3.2.12 on 2022-05-02 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bti', '0005_auto_20220402_2353'),
        ('app_v1', '0002_auto_20220423_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceTrack',
            fields=[
                ('id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm', models.CharField(max_length=60)),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_processing', models.BooleanField(db_index=True, default=False)),
                ('flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bti.flow')),
            ],
            options={
                'abstract': False,
                'unique_together': {('firm', 'identifier')},
            },
        ),
    ]
