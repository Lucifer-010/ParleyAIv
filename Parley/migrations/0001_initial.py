# Generated by Django 4.2.10 on 2024-05-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=5000)),
                ('response', models.CharField(max_length=5000)),
            ],
        ),
    ]
