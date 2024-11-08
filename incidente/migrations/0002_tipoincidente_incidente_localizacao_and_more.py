# Generated by Django 5.1.2 on 2024-11-02 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='incidente',
            name='localizacao',
            field=models.CharField(default='Não definida', max_length=50),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidente.tipoincidente'),
        ),
    ]
