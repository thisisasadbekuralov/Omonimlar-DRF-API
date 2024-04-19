# Generated by Django 4.2.11 on 2024-04-19 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Word Types',
                'db_table': 'word_types',
            },
        ),
        migrations.CreateModel(
            name='Homonyms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('origin', models.CharField(blank=True, max_length=100, null=True)),
                ('meaning', models.CharField(max_length=100)),
                ('example', models.CharField(blank=True, max_length=100, null=True)),
                ('word_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_homonyms.wordtype')),
            ],
            options={
                'verbose_name_plural': 'Homonyms',
                'db_table': 'homonyms',
                'ordering': ['id'],
            },
        ),
    ]
