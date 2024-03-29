from datetime import datetime
from django.utils import timezone

import os
from pprint import pprint

from .models import PurchaseBook
from .tests.data import json_data as get_data

from .sii import SiiScraper
from .models import PurchaseBook


def format_document(document):
    return {
        'codigo_iva_no_rec': document['Codigo IVA No Rec.'],
        'codigo_otro_impuesto': document['Codigo Otro Impuesto'],
        'fecha_acuse': datetime.strptime(document['Fecha Acuse'], '%d/%m/%Y') if document['Fecha Acuse'] else None,
        'fecha_docto': datetime.strptime(document['Fecha Docto'], '%d/%m/%Y') if document['Fecha Docto'] else None,
        'fecha_recepcion': timezone.make_aware(datetime.strptime(document['Fecha Recepcion'], '%d/%m/%Y %H:%M:%S')) if document['Fecha Recepcion'] else None,
        'iva_activo_fijo': int(document['IVA Activo Fijo']) if document['IVA Activo Fijo'] else None,
        'iva_no_retenido': int(document['IVA No Retenido']) if document['IVA No Retenido'] else None,
        'iva_uso_comun': int(document['IVA uso Comun']) if document['IVA uso Comun'] else None,
        'impto_sin_derecho_credito': int(document['Impto. Sin Derecho a Credito']) if document['Impto. Sin Derecho a Credito'] else None,
        'monto_exento': int(document['Monto Exento']) if document['Monto Exento'] else None,
        'monto_iva_recuperable': int(document['Monto IVA Recuperable']) if document['Monto IVA Recuperable'] else None,
        'monto_iva_no_recuperable': int(document['Monto Iva No Recuperable']) if document['Monto Iva No Recuperable'] else None,
        'monto_neto': int(document['Monto Neto']) if document['Monto Neto'] else None,
        'monto_neto_activo_fijo': int(document['Monto Neto Activo Fijo']) if document['Monto Neto Activo Fijo'] else None,
        'monto_total': int(document['Monto Total']) if document['Monto Total'] else None,
        'nce_nde_sobre_fact_compra': int(document['NCE o NDE sobre Fact. de Compra']) if document['NCE o NDE sobre Fact. de Compra'] else None,
        'razon_social': document['Razon Social'],
        'tabacos_cigarrillos': document['Tabacos Cigarrillos'],
        'tabacos_elaborados': document['Tabacos Elaborados'],
        'tabacos_puros': document['Tabacos Puros'],
        'tasa_otro_impuesto': document['Tasa Otro Impuesto'],
        'tipo_compra': document['Tipo Compra'],
        'tipo_doc': document['Tipo Doc'],
        'valor_otro_impuesto': int(document['Valor Otro Impuesto']) if document['Valor Otro Impuesto'] else None,
    }


def purchase_book():

    # rut = os.getenv('SII_RUT', '77127941-4')
    # password = os.getenv('SII_PASSWORD', 'Mateo2015')


    # sii_client = SiiScraper(full_rut=rut, clave=password)

    # json_data = sii_client.get_book()

    json_data = get_data


    for document_data in json_data:
        folio = document_data['Folio']
        rut_proveedor = document_data['RUT Proveedor']
        
        formatted_document = format_document(document_data)

        existing_document = PurchaseBook.objects.filter(folio=folio, rut_proveedor=rut_proveedor).first()
        
        if existing_document:
            print(f'Updating document with folio {folio}')
            # Document already exists, update the fields
            for field, value in formatted_document.items():

                setattr(existing_document, field, value)

            existing_document.save()


        else:
            print(f'Creating document with folio {folio}')
            # Document does not exist, create a new one
            PurchaseBook.objects.create(folio=folio, rut_proveedor=rut_proveedor, **formatted_document)






