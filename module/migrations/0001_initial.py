# Generated by Django 4.1 on 2022-09-02 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('schedule', models.TimeField()),
                ('students', models.ManyToManyField(related_name='students', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='module', to='module.class')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
