# Generated by Django 4.2.6 on 2023-11-03 23:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wfavicon", "0003_alter_faviconsettings_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faviconsettings",
            name="app_name",
        ),
        migrations.RemoveField(
            model_name="faviconsettings",
            name="app_theme_color",
        ),
    ]