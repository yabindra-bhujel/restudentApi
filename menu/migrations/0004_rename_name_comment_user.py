# Generated by Django 4.2 on 2023-04-09 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]
