# Generated by Django 4.1.7 on 2023-03-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_alter_questionchoice_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoice',
            name='choice_text',
            field=models.CharField(max_length=150),
        ),
    ]
