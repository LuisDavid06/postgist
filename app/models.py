from django.contrib.gis.db import models


# Create your models here.

class MainTb001Plans(models.Model):
    id = models.BigAutoField(primary_key=True)
    plan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed=True,
        db_table='main_tb001_planes'

    def __str__(self):
        return self.plan.upper()

class MainTb002Zone(models.Model):
    id = models.BigAutoField(primary_key=True)
    zone = models.GeometryField()
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed=True,
        db_table='main_tb002_zonas'

    def __str__(self):
        return str(self.name).upper()


class MainTb003ZoneHasPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    zone_id = models.ForeignKey('MainTb002Zone', on_delete=models.CASCADE, db_column='zone_id', blank=True, null=True )
    plan_id = models.ForeignKey('MainTb001Plans', on_delete=models.CASCADE, db_column='plan_id', blank=True, null=True )
    class Meta:
        managed=True,
        db_table='main_tb003_zona_has_planes'

    def __str__(self):
        return str(self.id)