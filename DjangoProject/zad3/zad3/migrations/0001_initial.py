# Generated by Django 4.2.9 on 2024-01-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YourTable',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('continuous_feature1', models.FloatField()),
                ('continuous_feature2', models.FloatField()),
                ('categorical_feature', models.IntegerField()),
            ],
        ),
    ]
