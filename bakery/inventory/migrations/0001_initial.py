# Generated by Django 3.0.6 on 2020-12-29 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BakeryItemIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_percentage', models.CharField(max_length=5)),
                ('bakery_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.BakeryItem')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='bakeryitem',
            name='ingredients',
            field=models.ManyToManyField(through='inventory.BakeryItemIngredient', to='inventory.Ingredient'),
        ),
    ]
