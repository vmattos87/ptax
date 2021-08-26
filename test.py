import unittest
import requests
from foo import query, save

url = 'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do'
params = {'method': 'consultarBoletim',
                                'RadOpcao': '1',
                                'ChkMoeda': '',
                                'DATAINI': '02/01/2020',
                                'DATAFIM': '02/02/2020'}


class TestCase(unittest.TestCase):

    def test_request_response(self):
        response = requests.get('https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim')
        self.assertTrue(response.ok)

    def test_response_success(self):
        response = requests.get('https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_get_content_usd(self):
        params['ChkMoeda'] = '61'
        self.assertIsNotNone(query.fetch(url, params))

    def test_get_content_eur(self):
        params['ChkMoeda'] = '222'
        self.assertIsNotNone(query.fetch(url, params))

    def test_is_data_valid_usd(self):
        params['ChkMoeda'] = '61'
        rows = query.fetch(url, params)
        self.assertIsNotNone(rows)
        self.assertTrue(query.get_values_USD(rows))

    def test_is_data_valid_eur(self):
        params['ChkMoeda'] = '222'
        rows = query.fetch(url, params)
        self.assertIsNotNone(rows)
        self.assertTrue(query.get_values_EUR(rows))

    def test_save_usd(self):
        params['ChkMoeda'] = '61'
        rows = query.fetch(url, params)
        self.assertIsNotNone(rows)
        self.assertTrue(save.save_CSV_USD(rows))
    
    def test_save_eur(self):
        params['ChkMoeda'] = '222'
        rows = query.fetch(url, params)
        self.assertIsNotNone(rows)
        self.assertTrue(save.save_CSV_EUR(rows))
    
        