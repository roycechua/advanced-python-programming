# Generated by Django 2.0.5 on 2019-05-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_title', models.CharField(max_length=200)),
                ('training_content', models.TextField()),
                ('training_schedule', models.DateTimeField(verbose_name='Training Schedule')),
            ],
        ),
    ]