# Generated by Django 4.0.5 on 2022-06-16 19:18

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.expressions.ExpressionList, to='crud.task'),
        ),
    ]
