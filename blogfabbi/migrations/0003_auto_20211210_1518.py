# Generated by Django 3.0.7 on 2021-12-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfabbi', '0002_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]