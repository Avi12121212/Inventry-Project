# Generated by Django 4.0.4 on 2022-08-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('model', models.CharField(max_length=200)),
                ('feature', models.CharField(max_length=200)),
                ('camera', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'phone',
            },
        ),
    ]
