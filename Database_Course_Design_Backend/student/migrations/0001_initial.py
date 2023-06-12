# Generated by Django 4.2.2 on 2023-06-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("sex", models.CharField(max_length=10)),
                ("student_id", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=50)),
                ("class_name", models.CharField(max_length=50)),
                ("telephone", models.CharField(max_length=20)),
            ],
        ),
    ]