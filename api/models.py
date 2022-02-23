from unicodedata import name
from django.db import models

# Create your models here.

class SupportedApp(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class RiskParam(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class RiskRecomendation(models.Model):
    name = models.CharField(max_length=255)
    param_id = models.ForeignKey(RiskParam, on_delete=models.CASCADE, related_name="risk_recomendations")
    

class SupportedAppParam(models.Model):
    app_id = models.ForeignKey(SupportedApp, on_delete=models.CASCADE,related_name="supported_app_params")
    param_id = models.ForeignKey(RiskParam, on_delete=models.DO_NOTHING, related_name="supported_app_params")



