# Generated by Django 3.2.4 on 2021-06-26 02:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 26, 2, 28, 59, 363940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('comment_time', models.DateTimeField(default=datetime.datetime(2021, 6, 26, 2, 28, 59, 363940, tzinfo=utc))),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['comment_time'],
            },
        ),
    ]
