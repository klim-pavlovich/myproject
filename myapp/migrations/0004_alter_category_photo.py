# Generated by Django 5.1.2 on 2024-11-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_coocking_steps_recipe_cooking_steps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='default_image.png', upload_to='category_photos/'),
        ),
    ]
