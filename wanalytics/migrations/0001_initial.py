# Generated by Django 4.1.1 on 2023-10-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnalyticsSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ga_g_tracking_id",
                    models.CharField(
                        blank=True,
                        help_text='Your Google Analytics 4 tracking ID (begins with "G-")',
                        max_length=255,
                        verbose_name="G Tracking ID",
                    ),
                ),
                (
                    "gtm_id",
                    models.CharField(
                        blank=True,
                        help_text='Begins with "GTM-"',
                        max_length=255,
                        verbose_name="Google Tag Manager ID",
                    ),
                ),
                (
                    "gads_id",
                    models.CharField(
                        blank=True,
                        help_text='Begins with "AW-"',
                        max_length=255,
                        verbose_name="Google Ads ID",
                    ),
                ),
                (
                    "head_scripts",
                    models.TextField(
                        blank=True,
                        help_text="Add tracking scripts between the <head> tags.",
                        null=True,
                        verbose_name="<head> tracking scripts",
                    ),
                ),
                (
                    "body_scripts",
                    models.TextField(
                        blank=True,
                        help_text="Add tracking scripts toward closing <body> tag.",
                        null=True,
                        verbose_name="<body> tracking scripts",
                    ),
                ),
            ],
            options={
                "verbose_name": "Analytics",
            },
        ),
    ]
