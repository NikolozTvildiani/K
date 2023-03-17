# Generated by Django 4.1.7 on 2023-03-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_number', models.IntegerField(null=True)),
                ('choosen_answer', models.IntegerField(blank=True, null=True)),
                ('answer_state', models.IntegerField(choices=[(1, 'Unseen'), (2, 'Seen'), (3, 'Answered'), (4, 'Correct'), (5, 'Incorrect'), (6, 'Unselected Timeout'), (7, 'Selected Timeout')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('choosen_answer_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.questionchoice')),
                ('wrd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiles.writerequestdata')),
            ],
        ),
    ]
