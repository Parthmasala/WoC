# Generated by Django 4.0 on 2022-01-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_App', '0004_delete_participantreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(max_length=30)),
                ('participant_contact', models.CharField(max_length=10)),
                ('participant_email', models.CharField(max_length=20)),
                ('select_event', models.CharField(max_length=30)),
                ('registration_type', models.CharField(max_length=30)),
                ('num_of_people', models.PositiveIntegerField()),
            ],
        ),
    ]