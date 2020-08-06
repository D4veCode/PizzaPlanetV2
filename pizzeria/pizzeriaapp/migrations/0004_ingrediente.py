# Generated by Django 3.1 on 2020-08-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaapp', '0003_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tamano', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
