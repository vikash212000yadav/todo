# Generated by Django 2.2.3 on 2019-07-21 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20190721_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='choice',
            new_name='status',
        ),
    ]