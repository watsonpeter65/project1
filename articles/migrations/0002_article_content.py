# Generated by Django 3.2.11 on 2022-01-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]