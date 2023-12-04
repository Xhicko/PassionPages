# Generated by Django 4.2.7 on 2023-11-30 14:30

import PassionPage_Users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('First_Name', models.CharField(max_length=15)),
                ('Last_Name', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=30)),
                ('slug', models.SlugField(default='default', max_length=250, unique_for_date='Publish')),
                ('Publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('Content', models.TextField()),
                ('Category_Tag', models.CharField(default='Default', max_length=20)),
                ('Image', models.ImageField(upload_to=PassionPage_Users.models.User_Directory_Path)),
                ('Status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='PassionPage_Users.category')),
            ],
            options={
                'ordering': ('-Publish',),
            },
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
