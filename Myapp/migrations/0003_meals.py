# Generated by Django 4.1.7 on 2023-03-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meals_type', models.CharField(max_length=50)),
            ],
        ),
    ]
