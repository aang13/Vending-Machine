# Generated by Django 3.0.4 on 2020-03-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine', '0002_transsactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transsactions',
            old_name='desired_products',
            new_name='inserted_amount',
        ),
        migrations.AlterField(
            model_name='transsactions',
            name='available_products',
            field=models.ManyToManyField(to='vending_machine.Products'),
        ),
    ]
