from django.db import models



type_doc = {
            '30': 'Factura',
            '32': 'Factura de ventas y servicios no afectos o exentos de IVA',
            '33': 'Factura Electrónica',
            '34': 'Factura no Afecta o Exenta Electrónica',
            '35': 'Total operaciones del mes, con boleta (afecta)',
            '38': 'Total operaciones del mes con boleta no afecta o exenta',
            '39': 'Total operaciones del mes, con boleta electrónica',
            '40': 'Liquidación factura',
            '41': 'Total operaciones del mes, con boleta no afecta o exenta electrónica',
            '43': 'Liquidación-Factura Electrónica',
            '45': 'Factura de Compra',
            '46': 'Factura de Compra electrónica.',
            '55': 'Nota de débito',
            '56': 'Nota de débito electrónica',
            '60': 'Nota de Crédito',
            '61': 'Nota de crédito electrónica',
            '101': 'Factura de exportación',
            '102': 'Factura de venta exenta a zona franca primaria',
            '103': 'Liquidación',
            '104': 'Nota de débito de exportación',
            '105': 'Boleta liquidación',
            '106': 'Nota de Crédito de exportación',
            '108': 'SRF Solicitud Registro de Factura',
            '109': 'Factura a turista',
            '110': 'Factura de Exportación Electrónica',
            '111': 'Nota de Débito de Exportación Electrónica',
            '112': 'Nota de Crédito de Exportación Electrónica',
            '901': 'Factura de ventas a empresas del territorio preferencial',
            '902': 'Conocimiento de Embarque (Marítimo o aéreo)',
            '903': 'Documento único de Salida (DUS)',
            '911': 'Declaración de Ingreso a Zona Franca Primaria',
            '914': 'Declaración de Ingreso (DIN)',
            '919': 'Resumen ventas de nacionales pasajes sin Factura',
            '920': 'Otros registros no documentados Aumenta débito',
            '922': 'Otros registros. Disminuye débito',
            '924': 'Resumen ventas de internacionales pasajes sin Factura'}


class PurchaseBook(models.Model):
    codigo_iva_no_rec = models.CharField(max_length=100, blank=True)
    codigo_otro_impuesto = models.CharField(max_length=100, blank=True)
    fecha_acuse = models.DateTimeField(blank=True, null=True)
    fecha_docto = models.DateField(blank=True, null=True)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    folio = models.CharField(max_length=100)

    iva_activo_fijo = models.IntegerField(blank=True, null=True)
    iva_no_retenido = models.IntegerField(blank=True, null=True)
    iva_uso_comun = models.IntegerField(blank=True, null=True)
    impto_sin_derecho_credito = models.IntegerField(blank=True, null=True)
    
    monto_exento = models.IntegerField(blank=True, null=True)
    monto_iva_recuperable = models.IntegerField(blank=True, null=True)
    monto_iva_no_recuperable = models.IntegerField(blank=True, null=True)
    monto_neto = models.IntegerField(blank=True, null=True)
    monto_neto_activo_fijo = models.IntegerField(blank=True, null=True)
    monto_total = models.IntegerField(blank=True, null=True)
    
    nce_nde_sobre_fact_compra = models.IntegerField(blank=True, null=True)
    rut_proveedor = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=200)

    tabacos_cigarrillos = models.CharField(max_length=100, blank=True)
    tabacos_elaborados = models.CharField(max_length=100, blank=True)
    tabacos_puros = models.CharField(max_length=100, blank=True)

    tasa_otro_impuesto = models.CharField(max_length=100, blank=True)
    tipo_compra = models.CharField(max_length=100)
    tipo_doc = models.CharField(max_length=6, choices=type_doc.items() )
    valor_otro_impuesto = models.IntegerField(blank=True, null=True)

    cost_centers = models.ManyToManyField('budgets.CostCenter', through='budgets.DocumentCostCenter')


    @property
    def tipo_documento(self):
        return type_doc.get(self.tipo_doc, 'Tipo de documento no encontrado')

    def __str__(self):
        return f'{self.folio} - {self.rut_proveedor} - {self.razon_social}'