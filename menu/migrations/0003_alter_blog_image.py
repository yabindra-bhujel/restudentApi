# Generated by Django 4.2 on 2023-04-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images'),
        ),
    ]
