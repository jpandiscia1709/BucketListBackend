# Generated by Django 3.2.8 on 2021-11-05 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adventures', '0001_initial'),
        ('bucketlist', '0003_auto_20211105_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interested', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Adventure',
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventures.adventure'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucketlist.bucketlist'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucketlist.bucketlist'),
        ),
        migrations.AddField(
            model_name='community',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]