# Generated by Django 2.1.7 on 2019-03-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('name', models.TextField()),
                ('amount', models.TextField()),
                ('note', models.TextField()),
                ('donateKey', models.TextField()),
            ],
        ),
    ]