# Generated by Django 4.1.1 on 2022-09-25 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_dropyou_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dropyou',
            old_name='user',
            new_name='person',
        ),
    ]
