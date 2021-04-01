# Generated by Django 3.1.7 on 2021-04-01 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=25)),
                ('skill_level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='characters',
            name='Char_Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='app_one.planets'),
        ),
    ]
