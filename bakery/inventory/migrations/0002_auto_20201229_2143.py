# Generated by Django 3.0.6 on 2020-12-29 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('count', models.PositiveSmallIntegerField()),
                ('bakery_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.BakeryItem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='bakeryitems',
            field=models.ManyToManyField(through='inventory.OrderItem', to='inventory.BakeryItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]