# Generated by Django 3.0.2 on 2020-03-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_auto_20200302_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]