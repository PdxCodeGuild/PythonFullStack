# Generated by Django 3.1.4 on 2021-02-02 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('send_newsletter', models.BooleanField()),
                ('age', models.IntegerField(null=True)),
                ('customer_points', models.FloatField()),
                ('date_of_birth', models.DateField(null=True)),
                ('date_joined', models.DateTimeField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.state'),
        ),
    ]
