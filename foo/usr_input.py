from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_date():

    while True:
        s_date = input('\nInforme a data inicial da pesquisa (dd/mm/yyyy): ')
        try:
            start_date = datetime.strptime(s_date, '%d/%m/%Y')

            if start_date < datetime(1984, 11, 28):
                print(
                    '\nPeríodo indisponível. Insira uma data a partir de 28/11/1984.\n')
                continue

            elif start_date.year < 2002:
                print(
                    '\nPeríodo indisponível para o Euro. Insira uma data a partir de 02/01/2002.\n')
                continue

            elif start_date > datetime.today():
                print(
                    f'\nPeríodo indisponível. Insira uma data até {datetime.today():%d/%m/%Y}\n')
                continue

            break

        except:
            print(
                '\nData inválida, insira uma data no formato indicado. Ex: 20/04/2020\n')

    max_date = start_date + relativedelta(months=+6)

    while True:
        e_date = input('\nInforme a data final da pesquisa (dd/mm/yyyy): ')
        try:
            end_date = datetime.strptime(e_date, '%d/%m/%Y')

            if end_date > datetime.today():
                print(
                    f'\nPeríodo indisponível. Insira uma data até {datetime.today():%d/%m/%Y}\n')
                continue

            elif end_date > max_date:
                print(
                    f'\nData inválida. O período deve ser menor ou igual a seis (6) meses!\n')
                continue

            elif end_date <= start_date:
                print(
                    f'\nPeríodo inválido. Insira uma data posterior a {start_date:%d/%m/%Y}\n')
                continue

            break

        except:
            print(
                '\nData inválida, insira uma data no formato indicado. Ex: 20/04/2020\n')

    return s_date, e_date


if __name__ == '__main__':
    pass
