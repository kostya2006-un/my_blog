# Generated by Django 4.2.4 on 2023-08-05 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added']},
        ),
    ]