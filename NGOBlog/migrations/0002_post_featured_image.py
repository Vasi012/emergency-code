# Generated by Django 3.2 on 2023-02-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
