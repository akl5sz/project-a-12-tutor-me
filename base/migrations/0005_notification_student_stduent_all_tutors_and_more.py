# Generated by Django 4.1.6 on 2023-04-15 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_mnem_course_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutor')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='stduent_all_tutors',
            field=models.ManyToManyField(through='base.Notification', to='base.tutor'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='tutor_all_students',
            field=models.ManyToManyField(through='base.Notification', to='base.student'),
        ),
    ]