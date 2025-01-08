# Generated by Django 5.1.4 on 2025-01-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_alter_tealeaves_collector_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tealeaves',
            name='collector_at',
        ),
        migrations.RemoveField(
            model_name='tealeaves',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tealeaves',
            name='quality',
        ),
        migrations.RemoveField(
            model_name='tealeaves',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='tealeaves',
            name='collector_name',
            field=models.CharField(max_length=100),
        ),
    ]