# Generated by Django 5.0.6 on 2024-06-27 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_alter_userinfo_options_alter_userinfo_father_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
