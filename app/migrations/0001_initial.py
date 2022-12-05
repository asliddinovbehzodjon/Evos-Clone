# Generated by Django 4.1.3 on 2022-11-28 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter category name', max_length=100, verbose_name='Category')),
                ('image', models.ImageField(help_text='Upload category image', upload_to='Category-Images', verbose_name='Category image')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category ',
                'verbose_name_plural': 'Categories ',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter product name', max_length=100, verbose_name='Product name')),
                ('image', models.ImageField(help_text='Upload product image', upload_to='Product-Images', verbose_name='Product image')),
                ('price', models.IntegerField(help_text='Enter category price', verbose_name='Product price')),
                ('discount', models.IntegerField(help_text='Enter product discount price', verbose_name='Product discount price')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(help_text='Choose category', on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product ',
                'verbose_name_plural': 'Products ',
                'db_table': 'Products',
            },
        ),
    ]
