# Generated by Django 5.1.4 on 2025-01-09 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivariety_description_chaivariety_pprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chaivariety',
            old_name='pprice',
            new_name='price',
        ),
    ]
