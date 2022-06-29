# Generated by Django 4.0.5 on 2022-06-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=100)),
                ('nombre', models.TextField(max_length=100)),
                ('apellido', models.TextField(max_length=100)),
                ('rut', models.TextField(max_length=100)),
                ('dvRut', models.TextField(max_length=100)),
                ('telefono', models.TextField(max_length=12)),
                ('contraseña', models.TextField(max_length=100)),
                ('contraseña2', models.TextField(max_length=100)),
                ('correo', models.TextField(max_length=100)),
                ('nacimiento', models.TextField(max_length=100)),
            ],
        ),
    ]
