# Generated by Django 3.2.9 on 2021-12-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_it', '0006_alter_blogpost_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnall',
            field=models.ImageField(default=1, upload_to='photo/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]