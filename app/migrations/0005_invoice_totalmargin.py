# Generated by Django 3.1.5 on 2021-08-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210821_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='totalmargin',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
