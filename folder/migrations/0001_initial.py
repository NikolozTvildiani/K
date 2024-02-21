# Generated by Django 4.1.7 on 2023-03-22 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import folder.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile_headline', models.CharField(max_length=128, validators=[folder.models.headline_unique])),
                ('pointer_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('subtype_of_tile', models.IntegerField(blank=True, null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('type_of_tile_char', models.CharField(choices=[('T', 'Tile/Tag'), ('B', 'Block'), ('O', 'Official Test'), ('S', 'Subject'), ('U', 'Organization'), ('K', 'Book'), ('C', 'Chapter'), ('P', 'Page'), ('C', 'Course'), ('R', 'Research Paper'), ('Q', 'Question')], max_length=1)),
                ('expected_reward', models.FloatField(blank=True, null=True)),
                ('total_questions', models.IntegerField(blank=True, null=True)),
                ('total_pass', models.IntegerField(default=0)),
                ('total_writes', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('children', models.ManyToManyField(blank=True, to='folder.tile')),
                ('questions', models.ManyToManyField(blank=True, to='questions.question')),
            ],
        ),
        migrations.CreateModel(
            name='WriteRequestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_reward', models.FloatField(default=1, null=True)),
                ('block_mode', models.IntegerField(choices=[(1, 'Test'), (2, 'Training')])),
                ('block_sector', models.IntegerField(choices=[(1, 'Private'), (2, 'Public')])),
                ('timed', models.BooleanField(default=False)),
                ('block_total_questions', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('total_correct', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tile_created_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder.tile')),
            ],
        ),
    ]