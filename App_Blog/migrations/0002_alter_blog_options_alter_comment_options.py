# Generated by Django 5.0.3 on 2024-04-02 16:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("App_Blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-publish_date"]},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-comment_date"]},
        ),
    ]