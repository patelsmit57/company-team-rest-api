# Generated by Django 4.1.1 on 2022-09-15 06:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('CEO', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('Inception_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Lead_Name', models.CharField(max_length=100)),
                ('CompanyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
            ],
        ),
    ]
