# Generated by Django 2.2.3 on 2020-03-02 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200301_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='order_name',
        ),
    ]
