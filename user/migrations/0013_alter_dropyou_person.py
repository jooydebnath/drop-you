# Generated by Django 4.1.1 on 2022-09-25 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_dropyou_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropyou',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.userprofile'),
        ),
    ]