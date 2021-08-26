import requests
from requests import get
from bs4 import BeautifulSoup
import re


def fetch(url, params):
    html = requests.get(url, params)
    soup = BeautifulSoup(html.text, 'html.parser')
    table = soup.find('table')

    rows = []
    for trow in table.find_all('tr')[:-1]:
        cols = trow.find_all('td')
        row = []
        for col in cols:
            row.append(col.text)
        if row != []:
            rows.append(row)

    return rows


def get_values_USD(rows):
    print('\nBoletim de cotações PTAX Dólar')

    for item in rows:
        date = re.search(
            r'([0-3]?[0-9]\/[0-1]?[0-9]\/(19|20)\d{2})', str(item))
        usd_rate = re.findall(r'([0-9]\,[0-9]{4})', str(item))
        usd_buy = usd_rate[0]
        usd_sell = usd_rate[1]

        try:
            assert re.match(
                r'([0-3]?[0-9]\/[0-1]?[0-9]\/(19|20)\d{2})', date.group())
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', usd_buy)
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', usd_sell)
        except AssertionError as err:
            print(err)
            return False

        print(date.group())
        print(f'Compra: {usd_buy}\nVenda: {usd_sell}\n\n')

    return True


def get_values_EUR(rows):
    print('\nBoletim de cotações PTAX Euro')

    for item in rows:
        date = re.search(
            r'([0-3]?[0-9]\/[0-1]?[0-9]\/(19|20)\d{2})', str(item))
        eur_rate = re.findall(r'([0-9]\,[0-9]{4})', str(item))

        eur_tax_buy = eur_rate[0]
        eur_tax_sell = eur_rate[1]
        eur_par_buy = eur_rate[2]
        eur_par_sell = eur_rate[3]

        try:
            assert re.match(
                r'([0-3]?[0-9]\/[0-1]?[0-9]\/(19|20)\d{2})', date.group())
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', eur_tax_buy)
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', eur_tax_sell)
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', eur_par_buy)
        except AssertionError as err:
            print(err)
            return False

        try:
            assert re.match(r'([0-9]\,[0-9]{4})', eur_par_sell)
        except AssertionError as err:
            print(err)
            return False

        print(date.group())
        print(f'Taxa\nCompra: {eur_tax_buy}\nVenda: {eur_tax_sell}\n')
        print(f'Paridade\nCompra: {eur_par_buy}\nVenda: {eur_par_sell}\n\n')

    return True


if __name__ == '__main__':
    pass
