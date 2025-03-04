# Generated by Django 5.0.3 on 2024-03-28 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sii', '0003_remove_purchasebook_nro'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='budgets.costcenter')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proportion', models.DecimalField(decimal_places=2, default=100, max_digits=5)),
                ('amount', models.IntegerField(default=0)),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgets.costcenter')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sii.purchasebook')),
            ],
        ),
    ]
