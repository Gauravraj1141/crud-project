# Generated by Django 4.1.4 on 2022-12-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=16),
        ),
    ]
