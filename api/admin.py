from django.contrib import admin
from .models import RiskParam, RiskRecomendation, SupportedApp, SupportedAppParam
# Register your models here.

@admin.register(RiskParam)
class RiskParamAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(SupportedApp)
class SupportedAppAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(RiskRecomendation)
class RiskRecomendationAdmin(admin.ModelAdmin):
    list_display = ["name","param_id"]

@admin.register(SupportedAppParam)
class SupportedAppParamAdmin(admin.ModelAdmin):
    list_display = ["app_id","param_id"]
