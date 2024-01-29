# Generated by Django 4.2.6 on 2023-11-08 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_id", models.CharField(max_length=50, unique=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("O1", "O1"),
                            ("O2", "O2"),
                            ("FE", "FE"),
                            ("FP", "FP"),
                            ("MS", "MS"),
                            ("PH", "PH"),
                            ("-", "-"),
                        ],
                        default="-",
                        max_length=3,
                    ),
                ),
                (
                    "group",
                    models.CharField(
                        choices=[("s", "s"), ("p", "p"), ("t", "t"), ("i", "i")],
                        default="-",
                        max_length=3,
                    ),
                ),
                (
                    "semester",
                    models.CharField(
                        choices=[("V", "V"), ("H", "H")], default="-", max_length=2
                    ),
                ),
                (
                    "studiepoeng",
                    models.FloatField(
                        choices=[
                            ("3,75", "3,75"),
                            ("7,5", "7,5"),
                            ("10,0", "10,0"),
                            ("15,0", "15,0"),
                            ("20,0", "20,0"),
                            ("30,0", "30,0"),
                        ],
                        max_length=4,
                    ),
                ),
                ("nb_student", models.IntegerField(null=True)),
                ("nb_vit", models.IntegerField(null=True)),
                ("nb_stud_ass", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "position",
                    models.CharField(
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
                (
                    "groupe",
                    models.CharField(
                        choices=[
                            ("s", "s"),
                            ("p", "p"),
                            ("t", "t"),
                            ("i", "i"),
                            ("Ext", "Ext"),
                        ],
                        default="-",
                        max_length=3,
                    ),
                ),
                (
                    "courses",
                    models.ManyToManyField(
                        related_name="courses", to="app_teaching.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersonCourse",
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
                ("amount", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_teaching.course",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_teaching.person",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Project",
        ),
    ]