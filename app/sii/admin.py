from django.contrib import admin

from .models import PurchaseBook

@admin.register(PurchaseBook)
class PurchaseBookAdmin(admin.ModelAdmin):
    
    list_display = ['folio', 'rut_proveedor', 'razon_social', 'fecha_docto', 'tipo_doc', 'formatted_monto_total']
    list_display_links = ['folio']
    list_filter = ['fecha_docto', 'tipo_doc']


    def formatted_monto_total(self, obj):
        return '{:,.0f}'.format(obj.monto_total).replace(',', '.')
    formatted_monto_total.short_description = 'Monto Total'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False