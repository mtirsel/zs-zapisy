# Generated by Django 2.1.5 on 2019-01-13 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('child_name', models.CharField(max_length=100)),
                ('parent_name', models.CharField(max_length=100)),
                ('child_brith_date', models.DateField()),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('identifier', models.CharField(blank=True, default='', max_length=10)),
                ('note', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('available', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='registrationanswer',
            name='reg_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='regform.RegistrationDate'),
        ),
    ]