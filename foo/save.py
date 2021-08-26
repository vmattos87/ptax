import re
import csv
import os


def save_CSV_USD(rows):
    header = ['Data', 'Tipo', 'Compra', 'Venda']

    start_date = re.sub(r'\/', '-', rows[0][0],)
    end_date = re.sub(r'\/', '-', rows[len(rows)-1][0])

    filename = 'PTAX_USD_' + start_date + '_' + end_date + '.csv'

    try:
        with open(filename, 'w', encoding='UTF8') as f:
            csv.register_dialect('semicolon-delimited')
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)
            writer.writerows(rows)
    except Exception as err:
        print('Ocorreu um erro ao salvar o arquivo.\n', err)
        return False

    print(f'\nSalvando consulta em {os.path.join(os.getcwd(), filename)}\n')

    return True


def save_CSV_EUR(rows):
    header = ['Data', 'Tipo', 'Taxa_Compra',
              'Taxa_Venda', 'Paridade_Compra', 'Paridade_Venda']

    start_date = re.sub(r'\/', '-', rows[0][0],)
    end_date = re.sub(r'\/', '-', rows[len(rows)-1][0])

    filename = 'PTAX_EUR_' + start_date + '_' + end_date + '.csv'

    try:
        with open(filename, 'w', encoding='UTF8') as f:
            csv.register_dialect('semicolon-delimited')
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)
            writer.writerows(rows)
    except Exception as err:
        print('Ocorreu um erro ao salvar o arquivo\n', err)
        return False

    print(f'\nSalvando consulta em {os.path.join(os.getcwd(), filename)}\n')

    return True


if __name__ == '__main__':
    pass
