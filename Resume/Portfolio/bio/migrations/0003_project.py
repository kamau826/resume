# Generated by Django 4.1.4 on 2022-12-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_alter_experience_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descr', models.TextField()),
                ('link', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
