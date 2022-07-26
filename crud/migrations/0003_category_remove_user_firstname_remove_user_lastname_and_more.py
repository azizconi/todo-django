# Generated by Django 4.0.5 on 2022-06-16 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_user_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='task',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(default='Angelina', max_length=255),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='crud.category'),
        ),
    ]
