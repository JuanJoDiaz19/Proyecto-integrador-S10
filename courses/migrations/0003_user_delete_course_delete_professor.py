# Generated by Django 4.2.6 on 2023-10-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
