# Generated by Django 3.2.8 on 2021-10-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=60)),
                ('Course_Number', models.IntegerField(blank=True, default='', max_length=10)),
                ('Instructor_Name', models.CharField(blank=True, default='', max_length=60)),
                ('Duration', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
        ),
    ]
