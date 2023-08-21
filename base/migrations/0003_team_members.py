# Generated by Django 4.2.4 on 2023-08-21 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_team_leader_team_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=3)),
                ('institute_details', models.TextField(blank=True, null=True)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.team')),
            ],
        ),
    ]
