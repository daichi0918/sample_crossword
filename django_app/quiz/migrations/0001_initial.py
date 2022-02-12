# Generated by Django 3.0.4 on 2022-02-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_img_src', models.CharField(max_length=100)),
                ('vertical', models.CharField(max_length=500)),
                ('horizontal', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=100)),
                ('answer_img_src', models.CharField(max_length=100)),
            ],
        ),
    ]