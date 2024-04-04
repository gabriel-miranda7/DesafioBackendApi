# Generated by Django 5.0.4 on 2024-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('ano', models.PositiveIntegerField()),
                ('cor', models.CharField(choices=[('Azul', 'Azul'), ('Branco', 'Branco'), ('Prata', 'Prata'), ('Preto', 'Preto'), ('Vermelho', 'Vermelho')], default='Preto', max_length=10)),
            ],
        ),
    ]
