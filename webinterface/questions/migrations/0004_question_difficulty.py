# Generated by Django 3.0.6 on 2020-05-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20200506_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Выберите сложность', max_length=50, verbose_name='Сложность'),
        ),
    ]
