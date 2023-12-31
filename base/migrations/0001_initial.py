# Generated by Django 4.1.6 on 2023-04-30 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=8)),
                ('number', models.CharField(default='0000', max_length=8)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTutored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='0', max_length=200)),
                ('course', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('hourly_rate', models.CharField(max_length=40)),
                ('time_frames', models.CharField(max_length=40)),
                ('tutor_all_courses', models.ManyToManyField(through='base.CourseTutored', to='base.course')),
                ('tutor_all_students', models.ManyToManyField(through='base.Notification', to='base.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student_all_tutors',
            field=models.ManyToManyField(through='base.Notification', to='base.tutor'),
        ),
        migrations.AddField(
            model_name='notification',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutor'),
        ),
        migrations.AddField(
            model_name='coursetutored',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutor'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_all_tutors',
            field=models.ManyToManyField(through='base.CourseTutored', to='base.tutor'),
        ),
    ]
