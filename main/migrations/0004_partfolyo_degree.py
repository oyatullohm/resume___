# Generated by Django 4.0.5 on 2022-07-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_partfolyo_t_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='partfolyo',
            name='degree',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
