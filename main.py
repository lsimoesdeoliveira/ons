import requests
import bs4
import datetime
import time
import csv

# Comentario com mudanças para GIT UHE

# Abre o histórico de geração e procura a última data com dados de medição
# with open(r'.\hist_hidraulicas.csv', newline='') as csvFile:
#     csvReader = csv.reader(csvFile, delimiter=';')
#     lastDate = list(csvReader)[-1][-0]
#     lastDate = datetime.datetime.strptime(lastDate, "%d/%m/%Y")
# csvFile.close()

# Última dada com registo
# d1 = lastDate.date()
d1 = datetime.date(2017, 5, 16)

# Procura no site do ONS as medições mais recentes
reqDate = requests.get('http://www.ons.org.br/resultados_operacao/SDRO/Diario/topo.htm')
reqDate.encoding = 'utf8'
soupDate = bs4.BeautifulSoup(reqDate.text, "html.parser")
textDate = soupDate.find_all('option')
textDate = textDate[1].get_text()
textDate = datetime.datetime.strptime(textDate[-10:], '%d/%m/%Y')
# d2 = textDate.date()
d2 = datetime.date(2017, 5, 16)

# Número de dias entre o último registro local e o disponível no ONS
deltaDias = (d2 - d1).days
dates = []

print('A última data de medições no arquivo local é: ', d1)
print('A última data de medições no site do ONS é: ', d2)

if input('Importar útimas medições? (S/N) ') == ('S' or 's'):

    # Gerando datas para a url
    for i in range(0, deltaDias + 1):
        dates.append((d1 + datetime.timedelta(days=i)).strftime("%Y_%m_%d"))
    url = 'http://www.ons.org.br/resultados_operacao/SDRO/Diario/'
    # complemento = '/HTML/08_ProducaoHidraulicaUsina.html'
    # Escolher dados a serem buscados
    # complemento = '/HTML/10_ProducaoEolicaUsina.html'     #(Endereço usado a partir de 16 de Maio de 2017)?
    complemento = '/HTML/09_ProducaoTermicaUsina.html'  # (Endereço usado a partir de 16 de Maio de 2017)?
    # complemento = '/HTML/08_ProducaoHidraulicaUsina.html' #(Endereço usado a partir de 16 de Maio de 2017)
    # complemento = '/HTML/09_ProducaoEolicaUsina.html'     #(Endereço usado até 15 de Maio de 2017)?
    # complemento = '/HTML/08_ProducaoTermicaUsina.html'    # (Endereço usado até 15 de Maio de 2017)?
    # complemento = '/HTML/07_ProducaoHidraulicaUsina.html' #(Endereço usado até 15 de Maio de 2017)

    for n in dates:
        urlCompleta = url + n + complemento
        res = requests.get(urlCompleta)

        if res.ok:
            res.encoding = 'utf8'

            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            text = soup.find_all('tbody')
            # A função anterior retorna um arry com todas as tabelas do frame
            # queremos a que contem os dados das usinas, supõe-se que seja a
            # maior.
            text = max(text, key=len)
            text = text.find_all('tr')

            i = 0
            n = datetime.datetime.strptime(n, "%Y_%m_%d").date().strftime("%d/%m/%Y")

            with open(r'.\hist_termicas.csv', 'a', newline='') as csvFile:
                csvWriter = csv.writer(csvFile, delimiter=';')
                for value in range(1, len(text) - 1):
                    linha = text[value].get_text().strip().replace(' \n\n', ';').replace('\n', ';')
                    linha = linha.split(';')
                    linha.insert(0, n)
                    csvWriter.writerow(linha)
            print('Dados de {} importados com sucesso'.format(n))
            csvFile.close()
            # Delay para evitar request negado pelo servidor

        else:
            print('/t ERRO: {1}, {2}: Dados de {0} com problemas.'.format(n, res.status_code, res.reason))

        time.sleep(1.5)
else:
    print('Nenhum dado importado')
    # tratar o cabeçalho
    # talvez importar os valores do find_all('tr')
