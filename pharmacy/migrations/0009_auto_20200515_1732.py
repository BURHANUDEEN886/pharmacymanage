# Generated by Django 3.0.3 on 2020-05-15 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0008_auto_20200514_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Medicine'),
        ),
    ]
