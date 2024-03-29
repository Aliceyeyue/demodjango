# Generated by Django 2.1.8 on 2019-10-17 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(upload_to='img')),
                ('phone', models.CharField(max_length=32)),
                ('fax', models.CharField(max_length=32)),
                ('post_code', models.CharField(max_length=32)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('picture', models.ImageField(upload_to='img')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Foods_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('time', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='img/upload')),
                ('content', models.TextField()),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(upload_to='img')),
                ('open_time', models.CharField(max_length=32)),
                ('stop_car', models.CharField(max_length=32)),
                ('address', models.TextField()),
                ('label', models.TextField()),
                ('foods_id', models.ManyToManyField(to='Foods.Foods')),
            ],
        ),
        migrations.AddField(
            model_name='foods',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foods.Foods_type'),
        ),
    ]
