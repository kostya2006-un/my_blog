# Generated by Django 4.2.4 on 2023-08-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(max_length=256, verbose_name='Тема поста'),
        ),
    ]
