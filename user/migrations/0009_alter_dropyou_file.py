# Generated by Django 4.1.1 on 2022-09-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_dropyou_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropyou',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
