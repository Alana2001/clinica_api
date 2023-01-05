# Generated by Django 4.1.4 on 2022-12-06 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastrar_Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('CRM', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.CharField(choices=[('1', '08:00 ás 09:00'), ('2', '09:00 ás 10:00'), ('3', '10:00 ás 11:00'), ('4', '14:00 ás 15:00'), ('5', '16:00 ás 17:00')], max_length=15)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.cadastrar_medicos', verbose_name='Cadastrar_Medicos')),
            ],
        ),
    ]
