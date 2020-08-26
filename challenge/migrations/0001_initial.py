# Generated by Django 3.1 on 2020-08-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('value', models.FloatField()),
                ('discount_value', models.FloatField(null=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]