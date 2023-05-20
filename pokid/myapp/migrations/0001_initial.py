# Generated by Django 4.2.1 on 2023-05-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('doctor_id', models.IntegerField(blank=True, null=True)),
                ('mac_address', models.TextField(blank=True, null=True)),
                ('child_name', models.TextField(blank=True, null=True)),
                ('child_surname', models.TextField(blank=True, null=True)),
                ('temp_min', models.FloatField(blank=True, null=True)),
                ('temp_max', models.FloatField(blank=True, null=True)),
                ('pulse_min', models.IntegerField(blank=True, null=True)),
                ('pulse_max', models.IntegerField(blank=True, null=True)),
                ('ox_min', models.IntegerField(blank=True, null=True)),
                ('ox_max', models.IntegerField(blank=True, null=True)),
                ('satur_min', models.IntegerField(blank=True, null=True)),
                ('satur_max', models.IntegerField(blank=True, null=True)),
                ('timer', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'child',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.TextField()),
                ('doctor_surname', models.TextField(blank=True, null=True)),
                ('work_place', models.TextField(blank=True, null=True)),
                ('phone_number', models.TextField(blank=True, null=True)),
                ('d_login', models.TextField(blank=True, null=True)),
                ('d_password', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('measure_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_saved', models.IntegerField(blank=True, null=True)),
                ('is_okay', models.IntegerField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('pulse', models.IntegerField(blank=True, null=True)),
                ('ox', models.IntegerField(blank=True, null=True)),
                ('satur', models.IntegerField(blank=True, null=True)),
                ('date_time', models.TextField(blank=True, null=True)),
                ('child_id', models.IntegerField()),
            ],
            options={
                'db_table': 'measure',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('date_time', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.IntegerField()),
                ('recipient', models.IntegerField()),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_login', models.TextField()),
                ('p_password', models.TextField(blank=True, null=True)),
                ('parent_name', models.TextField()),
                ('parent_surname', models.TextField()),
            ],
            options={
                'db_table': 'parent',
            },
        ),
    ]