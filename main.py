import requests
import bs4
import datetime
import time
import csv


# Comentario com mudanças para GIT UHE

# Abre o histórico de geração e procura a última data com dados de medição
with open(r'.\hist.csv', newline='') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    lastDate = list(csvReader)[-1][-0]
    lastDate = datetime.datetime.strptime(lastDate, "%d/%m/%Y")
csvFile.close()

# Procura no site do ONS as medições mais recentes
reqDate = requests.get('http://www.ons.org.br/resultados_operacao/SDRO/Diario/topo.htm')
reqDate.encoding = 'utf8'
soupDate = bs4.BeautifulSoup(reqDate.text, "html.parser")
textDate = soupDate.find_all('option')

# Lê a última data
textDate = textDate[1].get_text()
textDate = datetime.datetime.strptime(textDate[-10:], '%d/%m/%Y')

d1 = lastDate.date()
d2 = textDate.date()
delta = d2 - d1
dates = []

print('A última data de medições no arquivo local é: ', d1)
print('A última data de medições no site do ONS é: ', d2)

if input('Importar útimas medições? (S/N) ') == ('S' or 's'):

    for i in range(1, delta.days + 1):
        dates.append((d1 + datetime.timedelta(days=i)).strftime("%Y_%m_%d"))

    # Trechos da url para data scraping
    url = 'http://www.ons.org.br/resultados_operacao/SDRO/Diario/'
    complemento = '/HTML/09_ProducaoEolicaUsina.html'

    for n in dates:
        urlCompleta = url + n + complemento
        res = requests.get(urlCompleta)

        res.encoding = 'utf8'

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        text = soup.find_all('tr')

        i = 0
        n = datetime.datetime.strptime(n, "%Y_%m_%d").date().strftime("%d/%m/%Y")
        with open(r'.\hist.csv', 'a', newline='') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=';')

            for value in text:
                linha = value.get_text().strip().replace(' \n', ';').replace('\n', ';')
                linha = linha.split(';')
                linha = list(filter(bool, linha))
                if len(linha) == 4 and linha[0] != 'Submercado':
                    csvWriter.writerow(list([n, linha[0], linha[1]]))
                if linha[0] == 'Sistema Interligado Nacional':
                    break
        print('Dados de ' + n + ' importados com sucesso')
        csvFile.close()
        # Delay para evitar request negado pelo servidor
        time.sleep(1.5)

else:
    print('Nenhum dado importado')
    # tratar o cabeçalho
    # talvez importar os valores do find_all('tr')
