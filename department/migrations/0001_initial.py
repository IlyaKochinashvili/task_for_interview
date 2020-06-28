# Generated by Django 3.0.7 on 2020-06-23 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('department_code', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_mane', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=13)),
                ('status', models.BooleanField()),
                ('is_stuff', models.BooleanField(default=False)),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
    ]