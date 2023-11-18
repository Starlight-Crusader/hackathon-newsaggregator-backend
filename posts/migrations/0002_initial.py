# Generated by Django 4.2.7 on 2023-11-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TimeField()),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
    ]