# Generated by Django 5.1.2 on 2024-11-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_remove_course_category_course_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="isHome",
            field=models.BooleanField(default=False),
        ),
    ]
