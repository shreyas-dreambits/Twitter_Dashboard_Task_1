# Generated by Django 5.1.5 on 2025-02-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
