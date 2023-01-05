# Generated by Django 4.1.4 on 2022-12-06 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agendamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Consulta', to='medicos.agenda')),
                ('consulta_dos_clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente')),
            ],
        ),
    ]
