from pprint import pprint


data = [['IEV', '30', 'Factura'],
['IEV', '32', 'Factura de ventas y servicios no afectos o exentos de IVA'],
['IEV', '33', 'Factura Electrónica'],
['IEV', '34', 'Factura no Afecta o Exenta Electrónica'],
['IEV', '35', 'Total operaciones del mes, con boleta (afecta) Sólo en el resumen'],
['IEV', '38', 'Total operaciones del mes con boleta no afecta o exenta Sólo en el resumen'],
['IEV', '39', 'Total operaciones del mes, con boleta electrónica Sólo en el resumen'],
['IEV', '40', 'Liquidación factura'],
['IEV', '41', 'Total operaciones del mes, con boleta no afecta o exenta electrónica Sólo en el resumen'],
['IEV', '43', 'Liquidación-Factura Electrónica'],
['IEV', '45', 'Factura de Compra'],
['IEV', '46', 'Factura de Compra electrónica.'],
['IEV', '55', 'Nota de débito'],
['IEV', '56', 'Nota de débito electrónica'],
['IEV', '60', 'Nota de Crédito'],
['IEV', '61', 'Nota de crédito electrónica'],
['IEV', '101', 'Factura de exportación'],
['IEV', '102', 'Factura de venta exenta a zona franca primaria (Res. Ex. N° 601 de 07.05.82)'],
['IEV', '103', 'Liquidación'],
['IEV', '104', 'Nota de débito de exportación'],
['IEV', '105', 'Boleta liquidación (Res. Ex. N° 1423 del 23.12.76) Sólo en el resumen'],
['IEV', '106', 'Nota de Crédito de exportación'],
['IEV', '108', 'SRF Solicitud Registro de Factura'],
['IEV', '109', 'Factura a turista (Res. Ex. N° 6428 de 06.12.93)'],
['IEV', '110', 'Factura de Exportación Electrónica'],
['IEV', '111', 'Nota de Débito de Exportación Electrónica'],
['IEV', '112', 'Nota de Crédito de Exportación Electrónica'],
['IEV', '901', 'Factura de ventas a empresas del territorio preferencial ( Res. Ex. N°1057, del 25.04.85)'],
['IEV', '902', 'Conocimiento de Embarque (Marítimo o aéreo)'],
['IEV', '903', 'Documento único de Salida (DUS)'],
['IEV', '919', 'Resumen ventas de nacionales pasajes sin Factura Sólo en el resumen'],
['IEV', '920', 'Otros registros no documentados Aumenta débito Sólo en el resumen'],
['IEV', '922', 'Otros registros. Disminuye débito. Sólo en el resumen'],
['IEV', '924', 'Resumen ventas de internacionales pasajes sin Factura Sólo en el resumen'],
['IEC', '30', 'Factura'],
['IEC', '32', 'Factura de ventas y servicios no afectos o exentos de IVA'],
['IEC', '33', 'Factura Electrónica'],
['IEC', '34', 'Factura no Afecta o Exenta Electrónica'],
['IEC', '40', 'Liquidación Factura'],
['IEC', '43', 'Liquidación Factura Electrónica'],
['IEC', '45', 'Factura de Compra'],
['IEC', '46', 'Factura de Compra electrónica'],
['IEC', '55', 'Nota de Débito'],
['IEC', '56', 'Nota de débito electrónica'],
['IEC', '60', 'Nota de Crédito'],
['IEC', '61', 'Nota de crédito electrónica'],
['IEC', '108', 'SRF Solicitud de Registro de Factura'],
['IEC', '901', 'Factura de ventas a empresas del territorio preferencial ( Res. Ex. N° 1057, del 25.04.85)'],
['IEC', '914', 'Declaración de Ingreso (DIN)'],
['IEC', '911', 'Declaración de Ingreso a Zona Franca Primaria'],]

result_dict = {}

for item in data:
    if item[1] not in result_dict:
        result_dict[item[1]] = item[2]

pprint(result_dict)