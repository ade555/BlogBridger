# Generated by Django 5.0.1 on 2024-02-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='comment_author',
        ),
    ]