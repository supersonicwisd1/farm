# Generated by Django 4.1 on 2022-08-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.IntegerField()),
                ('delivery_type', models.CharField(choices=[('farm-to-door', 'Farm to door'), ('pickup', 'Pick Up')], max_length=300, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='crop.category')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]