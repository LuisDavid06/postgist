# Generated by Django 4.2.1 on 2023-05-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_maintb002zone_maintb003zonehasplans'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintb003zonehasplans',
            name='plan_id',
            field=models.ForeignKey(blank=True, db_column='plan_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.maintb001plans'),
        ),
    ]
