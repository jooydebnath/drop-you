# Generated by Django 4.1.1 on 2022-09-23 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_dropyou_text_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropyou',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.extraadd'),
        ),
    ]