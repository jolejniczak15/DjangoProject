# Generated by Django 4.2.9 on 2024-01-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zad3', '0003_delete_yourtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('continuous_feature1', models.FloatField()),
                ('continuous_feature2', models.FloatField()),
                ('categorical_feature', models.IntegerField()),
            ],
        ),
    ]