# Generated by Django 4.0.4 on 2022-06-11 18:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipTapFieldComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('node', models.CharField(max_length=255)),
                ('loc_from', models.PositiveIntegerField()),
                ('loc_to', models.PositiveIntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo_app.note', verbose_name='parent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
