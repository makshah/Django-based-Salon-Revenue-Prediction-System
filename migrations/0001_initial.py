# Generated by Django 2.1.2 on 2019-04-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=10000, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_contact', models.IntegerField(default=0)),
                ('customer_address', models.CharField(max_length=200)),
            ],
        ),
    ]
