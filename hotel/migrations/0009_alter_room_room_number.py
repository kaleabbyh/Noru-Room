# Generated by Django 4.0.3 on 2022-03-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_rename_room_image_room_room_image_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=200),
        ),
    ]
