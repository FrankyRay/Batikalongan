# Generated by Django 5.1.2 on 2024-10-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_reply_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='file_uploads/'),
        ),
    ]