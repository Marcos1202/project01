# Generated by Django 3.0.6 on 2020-09-21 23:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]