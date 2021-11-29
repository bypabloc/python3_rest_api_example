# Generated by Django 3.2.9 on 2021-11-29 00:58

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('last_login_at', models.DateTimeField(null=True)),
                ('last_ip_address', models.TextField(null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]