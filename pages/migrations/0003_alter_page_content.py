# Generated by Django 4.1.7 on 2023-02-22 01:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0002_alter_page_options_page_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="Contenido"),
        ),
    ]
