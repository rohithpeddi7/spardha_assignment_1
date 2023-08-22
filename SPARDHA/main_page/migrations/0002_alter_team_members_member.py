# Generated by Django 4.2.3 on 2023-08-22 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main_page", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team_members",
            name="member",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
