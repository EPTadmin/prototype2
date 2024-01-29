# Generated by Django 4.2.6 on 2023-11-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0009_alter_person_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="groupe",
            field=models.CharField(
                choices=[("s", "s"), ("p", "p"), ("t", "i"), ("Ext", "Ext")],
                default="-",
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="position",
            field=models.CharField(
                choices=[
                    ("P1", "P1"),
                    ("F1", "F1"),
                    ("UL", "UL"),
                    ("P2", "P2"),
                    ("F2", "F2"),
                    ("L", "L"),
                    ("Ext", "Ext"),
                ],
                default="-",
                max_length=3,
            ),
        ),
    ]
