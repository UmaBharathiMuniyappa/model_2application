# Generated by Django 4.2.6 on 2023-12-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.IntegerField()),
                ('cname', models.CharField(max_length=100)),
            ],
        ),
    ]
