# Generated by Django 4.2.10 on 2024-02-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('datetimefield', models.DateTimeField()),
                ('decimalfield', models.DecimalField(decimal_places=4, max_digits=20)),
                ('durationfield', models.DurationField()),
                ('file', models.FileField(upload_to='')),
                ('ip_address', models.GenericIPAddressField()),
                ('image', models.ImageField(upload_to='')),
                ('uuid', models.UUIDField()),
                ('json', models.JSONField()),
                ('positive_integer_big', models.PositiveIntegerField()),
                ('small_integer', models.PositiveSmallIntegerField()),
                ('Slugfield', models.SlugField()),
                ('agree', models.BooleanField(default=False)),
            ],
        ),
    ]
