# Generated by Django 4.0.4 on 2022-04-18 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drinks', '0002_drink_price_drink_pub_id'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('amount', models.PositiveSmallIntegerField()),
                ('send_date', models.DateField()),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfers', to='drinks.drink')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfers', to='users.user')),
            ],
        ),
    ]
