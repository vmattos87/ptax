from foo import query, save, usr_input


def get_USD(url, params):
    rows = query.fetch(url, params)
    if query.get_values_USD(rows):
        save.save_CSV_USD(rows)


def get_EUR(url, params):
    rows = query.fetch(url, params)
    if query.get_values_EUR(rows):
        save.save_CSV_EUR(rows)


url = 'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do'
COD_USD = '61'
COD_EUR = '222'

params = {'method': 'consultarBoletim',
          'RadOpcao': '1',
          'ChkMoeda': '',
          'DATAINI': '',
          'DATAFIM': ''}


def main():
    print('Consulta ao PTAX do Dólar e Euro\n')
    print('Após a consulta as cotações do Dólar e Euro serão salvas em arquivos .CSV\n\n')

    params['DATAINI'], params['DATAFIM'] = usr_input.get_date()

    params['ChkMoeda'] = COD_USD
    get_USD(url, params)

    params['ChkMoeda'] = COD_EUR
    get_EUR(url, params)


if __name__ == '__main__':
    main()
