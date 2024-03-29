import json
from datetime import datetime

import requests


class SiiScraper:

    _clave: str
    _rut: dict
    _token: str
    _cookies: str
    _session: requests.Session

    def __init__(self, full_rut: str, clave: str, period: str = None):
        self._rut = self._parse_rut(full_rut)
        self._clave = clave
        self._period = period

    def _parse_rut(self, full_rut: str) -> dict:
        return {
            'full': full_rut,
            'rut': full_rut[:-2].replace('.', ''),
            'dv': full_rut[-1],
        }

    def _sii_login(self):
        url = "https://zeusr.sii.cl/cgi_AUT2000/CAutInicio.cgi"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-ES,es;q=0.9,es-0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '124',  # Esto normalmente no es necesario añadir manualmente
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'zeusr.sii.cl',
            'Origin': 'https://zeusr.sii.cl',
            'Referer': 'https://zeusr.sii.cl/CAUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misiir/siihome.cgi',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.0.0 Safari/537.36'
        }

        payload = {
            'rut': self._rut['rut'],
            'dv': self._rut['dv'],
            '411': '',
            'rutcntr': self._rut['full'],
            'clave': self._clave,
            'referencia': 'https://misiir.sii.cl/cgi_misii/siihome.cgi',
            'bt_ingresar': 'bt_ingresar',
        }
        self._session.post(url, headers=headers, data=payload)
        cookies = self._session.cookies.get_dict()
        self._token = cookies['TOKEN']
        self._cookies = ';'.join(['%s=%s' % (name, value) for (name, value) in cookies.items()])

    def _get_book(self, period: str):
        url = 'https://www4.sii.cl/consdcvinternetui/services/data/facadeService/getDetalleCompraExport'

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,es-ES;q=0.9,es;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': self._cookies,
            'Host': 'www4.sii.cl',
            'Origin': 'https://www4.sii.cl',
            'Referer': 'https://www4.sii.cl/consdcvinternetui/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        data = {
            "metaData": {
                "namespace": "cl.sii.sdi.lob.diii.consdcv.data.api.interfaces.FacadeService/getDetalleCompraExport",
                "conversationId": self._token,
                "transactionId": "1",
                "page": None
            },
            "data": {
                "codTipoDoc": "0",
                "rutEmisor": self._rut['rut'],
                "dvEmisor": self._rut['dv'],
                "ptributario": period,
                "estadoContab": "REGISTRO",
                "operacion": "COMPRA",
                "busquedaInicial": True
            }
        }
        r2 = self._session.post(url, headers=headers, data=json.dumps(data))

        return self._parse_book(r2.json())

    def _parse_book(self, book: dict):
        data = book['data']
        headers = data[0].split(';')
        json_data = []

        for line in data[1:]:
            values = line.split(';')
            json_data.append(dict(zip(headers, values)))

        return json_data


    def get_book(self):
        self._session = requests.Session()
        self._sii_login()

        if self._period is None:
            ## set actual period
            now = datetime.now()
            period = f'{now.year}{now.month:02}' # 202107
            return self._get_book(period)

        return self._get_book(self._period)