# Generated by Django 3.2 on 2022-08-19 00:16

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
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='budget')),
                ('price', models.BigIntegerField(verbose_name='price of project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.FileField(upload_to='files/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'pending'), (1, 'open'), (2, 'no freelancer selected'), (3, 'closed'), (4, 'awaiting acceptance'), (5, 'accepted'), (6, 'in progress'), (7, 'completed'), (8, 'incomplete')], default=0, verbose_name='status of project')),
                ('expire_time', models.DateTimeField(verbose_name='expire time of project')),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.budget', verbose_name='project budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='jobs.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='jobs.project')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='jobs.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectFileInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='jobs.file')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='jobs.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
