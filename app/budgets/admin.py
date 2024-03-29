from django.contrib import admin

from .models import CostCenter, DocumentCostCenter

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'active']


@admin.register(DocumentCostCenter)
class DocumentCostCenterAdmin(admin.ModelAdmin):
    list_display = ['document', 'cost_center', 'proportion', 'amount']