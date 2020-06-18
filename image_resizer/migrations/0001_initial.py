# Generated by Django 3.0.7 on 2020-06-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResizeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_started', 'never started'), ('processing', 'processing'), ('done', 'done')], default='not_started', max_length=15)),
                ('target_width', models.PositiveSmallIntegerField()),
                ('target_height', models.PositiveSmallIntegerField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]