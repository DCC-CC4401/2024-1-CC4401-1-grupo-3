# Generated by Django 3.2.25 on 2024-07-10 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estadobuxef', '0003_reporte_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estadobuxef.estudiante'),
        ),
    ]