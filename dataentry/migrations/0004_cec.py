# Generated by Django 5.0.6 on 2024-10-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='CEC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('student', 'Student'), ('staff', 'Staff')], max_length=10)),
            ],
        ),
    ]
