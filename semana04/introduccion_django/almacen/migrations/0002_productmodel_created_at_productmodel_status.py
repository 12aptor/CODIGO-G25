# Generated by Django 5.0.7 on 2024-08-07 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]