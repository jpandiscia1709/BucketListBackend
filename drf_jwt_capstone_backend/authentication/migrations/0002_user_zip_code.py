# Generated by Django 3.2.8 on 2021-11-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(default=23451, max_length=5),
            preserve_default=False,
        ),
    ]