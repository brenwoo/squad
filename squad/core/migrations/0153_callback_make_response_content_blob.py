# Generated by Django 2.2.17 on 2021-03-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0152_add_build_patch_notified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='response_content',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
