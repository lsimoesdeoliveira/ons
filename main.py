import requests
import bs4
import datetime
import time
import csv

# branch geração UHE

# Complementos de dados a serem buscados
#    # complement = '/HTML/10_ProducaoEolicaUsina.html'      # (Endereço usado a partir de 16 de Maio de 2017)
#    # complement = '/HTML/09_ProducaoTermicaUsina.html'     # (Endereço usado a partir de 16 de Maio de 2017)
#    # complement = '/HTML/08_ProducaoHidraulicaUsina.html'  # (Endereço usado a partir de 16 de Maio de 2017)

#    # complement = '/HTML/09_ProducaoEolicaUsina.html'      # (Endereço usado até 15 de Maio de 2017)
#    # complement = '/HTML/08_ProducaoTermicaUsina.html'     # (Endereço usado até 15 de Maio de 2017)
#    # complement = '/HTML/07_ProducaoHidraulicaUsina.html'  # (Endereço usado até 15 de Maio de 2017)

menu = {
    'UHE': [r'.\hist_hidraulicas.csv', r'/HTML/08_ProducaoHidraulicaUsina.html'],
    'UTE': [r'.\hist_termicas.csv', r'/HTML/09_ProducaoTermicaUsina.html'],
    'EOL': [r'.\hist_eolicas.csv', r'/HTML/10_ProducaoEolicaUsina.html']
}

while True:
    FILE_MENU = input('Escolha os dados a serem atualizados (UHE ou UTE ou EOL): ').upper()
    if FILE_MENU in menu.keys():
        print('Você escolheu {}'.format(FILE_MENU))
        print('Isso causa a arbertura do arquivo {} e do complemento {}'.format(menu[FILE_MENU][0], menu[FILE_MENU][1]))
        break
    else:
        continue

arquivo = menu[FILE_MENU][0]
complement = menu[FILE_MENU][1]
url = 'http://www.ons.org.br/resultados_operacao/SDRO/Diario/'


def find_last_date_csv(path_to_file):
    # Abre o histórico de geração e procura a última data com dados de medição
    with open(path_to_file, newline='') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=';')
        lastDate = list(csvReader)[-1][-0]
        lastDate = datetime.datetime.strptime(lastDate, "%d/%m/%Y")
    csvFile.close()
    return lastDate.date()


def find_last_date_ons_site():
    # Procura no site do ONS as medições mais recentes
    reqDate = requests.get('http://www.ons.org.br/resultados_operacao/SDRO/Diario/topo.htm')
    reqDate.encoding = 'utf8'
    soupDate = bs4.BeautifulSoup(reqDate.text, "html.parser")
    textDate = soupDate.find_all('option')
    textDate = textDate[1].get_text()
    textDate = datetime.datetime.strptime(textDate[-10:], '%d/%m/%Y')
    return textDate.date()


def generate_dates_url(d1, numDays):
    # Gerando datas para a url
    dates = []
    for i in range(1, numDays + 1):
        dates.append((d1 + datetime.timedelta(days=i)).strftime("%Y_%m_%d"))
    return dates


# Entrada de datas específicas para testes
# d1 = datetime.date(2017, 5, 16)
# d2 = datetime.date(2017, 5, 31)
d1 = find_last_date_csv(arquivo)
d2 = find_last_date_ons_site()

print('A última data de medições no arquivo local é: {}'.format(d1))
print('A última data de medições no site do ONS é: {}'.format(d2))

numDays = (d2 - d1).days
dates = generate_dates_url(d1, numDays)

if (input('Importar útimas medições? (S/N) ').upper() == ('S')) and (numDays > 0):

    with open(arquivo, 'a', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=';')

        for date in dates:
            urlFull = url + date + complement
            res = requests.get(urlFull)
            n = datetime.datetime.strptime(date, "%Y_%m_%d").date().strftime("%d/%m/%Y")

            if res.ok:
                res.encoding = 'utf8'
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                text = soup.find_all('tbody')
                # A função anterior retorna um arry com todas as tabelas do frame
                # queremos a que contem os dados das usinas, supõe-se que seja a
                # maior.
                text = max(text, key=len)
                text = text.find_all('tr')

                for value in range(1, len(text) - 1):
                    linha = text[value].get_text().strip().replace(' \n\n', ';').replace('\n', ';')
                    linha = linha.split(';')
                    linha.insert(0, n)
                    csvWriter.writerow(linha)

                print('Dados de {} importados com sucesso'.format(n))

            else:
                print('/t ERRO: {1}, {2}: Dados de {0} com problemas.'.format(n, res.status_code, res.reason))
            # Delay para evitar request negado pelo servidor
            time.sleep(0.5)
    csvFile.close()

else:
    print('Nenhum dado importado')
