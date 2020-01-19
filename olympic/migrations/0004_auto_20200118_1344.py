# Generated by Django 3.0.2 on 2020-01-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0003_auto_20200117_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='age',
            field=models.TextField(verbose_name='Age of Athlete'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.TextField(verbose_name='Height of Athlete'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='noc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic.NOC'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.TextField(verbose_name='Weight of Athlete'),
        ),
    ]