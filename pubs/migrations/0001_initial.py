# Generated by Django 4.0.4 on 2022-04-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubname', models.CharField(max_length=100)),
                ('balance', models.IntegerField(null=True)),
                ('image', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
