# Generated by Django 3.2.14 on 2022-08-25 15:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('strada1949', '0004_alter_order_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Order ID'),
        ),
    ]
