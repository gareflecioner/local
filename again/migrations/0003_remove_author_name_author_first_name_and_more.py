# Generated by Django 5.0.6 on 2024-05-31 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('again', '0002_alter_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
