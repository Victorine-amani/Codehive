# Generated by Django 3.2.4 on 2021-09-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField(null=True)),
                ('class_name', models.CharField(blank=True, max_length=9, null=True)),
                ('identification', models.CharField(max_length=13)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Binary', 'Binary'), ('Do not specify', 'Do not specify'), ('They/Them', 'They/Them')], default='Female', max_length=20)),
                ('nationality', models.CharField(choices=[('Kenyan', 'Kenyan'), ('Ugandan', 'Ugandan'), ('Rwandese', 'Rwandese'), ('South Sudanese', 'South Sudanese'), ('Tanzanian', 'Tanzanian')], default='Kenyan', max_length=20)),
                ('room_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('guardian_phoneNumber', models.CharField(max_length=15)),
                ('academic_year', models.PositiveSmallIntegerField(default=2021)),
                ('city', models.CharField(max_length=15)),
                ('guardian_name', models.CharField(max_length=25)),
                ('profile_picture', models.ImageField(upload_to='media/')),
                ('medical_report', models.FileField(upload_to='media/')),
            ],
        ),
    ]
