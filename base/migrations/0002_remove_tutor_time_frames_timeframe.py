# Generated by Django 4.1.6 on 2023-05-01 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='time_frames',
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutor')),
            ],
        ),
    ]
