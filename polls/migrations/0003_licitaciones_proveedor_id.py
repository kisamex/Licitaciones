# Generated by Django 2.1.1 on 2018-08-31 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180831_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='licitaciones',
            name='proveedor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.proveedor'),
            preserve_default=False,
        ),
    ]
