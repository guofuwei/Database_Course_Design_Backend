# Generated by Django 4.2.2 on 2023-06-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HardResource",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("resource_name", models.CharField(max_length=100)),
                ("resource_num", models.IntegerField()),
            ],
        ),
    ]
