# Generated by Django 4.1.7 on 2023-02-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("title", models.CharField(max_length=200, verbose_name="Titulo")),
                ("content", models.TextField(verbose_name="Contenido")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Fecha edición"),
                ),
            ],
            options={
                "verbose_name": "página",
                "verbose_name_plural": "páginas",
                "ordering": ["title"],
            },
        ),
    ]
