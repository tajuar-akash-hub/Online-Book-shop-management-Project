# Generated by Django 5.0 on 2024-02-17 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_model_categories'),
        ('catagories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category_model',
        ),
    ]
