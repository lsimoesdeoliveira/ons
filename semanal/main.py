import requests
import bs4
import datetime
import time
import csv


# Complementos de dados a serem buscados
#    # complement = '/HTML/10_ProducaoEolicaUsina.html'      # (Endereço usado a partir de 16 de Maio de 2017)
#    # complement = '/HTML/09_ProducaoTermicaUsina.html'     # (Endereço usado a partir de 16 de Maio de 2017)
#    # complement = '/HTML/08_ProducaoHidraulicaUsina.html'  # (Endereço usado a partir de 16 de Maio de 2017)

#    # complement = '/HTML/09_ProducaoEolicaUsina.html'      # (Endereço usado até 15 de Maio de 2017)
#    # complement = '/HTML/08_ProducaoTermicaUsina.html'     # (Endereço usado até 15 de Maio de 2017)
#    # complement = '/HTML/07_ProducaoHidraulicaUsina.html'  # (Endereço usado até 15 de Maio de 2017)

# menu = {
    # 'UHE': [r'.\hist_hidraulicas.csv', r'/HTML/08_ProducaoHidraulicaUsina.html'],
    # 'UTE': [r'.\hist_termicas.csv', r'/HTML/09_ProducaoTermicaUsina.html'],
    # 'EOL': [r'.\hist_eolicas.csv', r'/HTML/10_ProducaoEolicaUsina.html']
# }

# while True:
    # FILE_MENU = input('Escolha os dados a serem atualizados (UHE ou UTE ou EOL): ').upper()
    # if FILE_MENU in menu.keys():
        # print('Você escolheu {}'.format(FILE_MENU))
        # print('Isso causa a arbertura do arquivo {} e do complemento {}'.format(menu[FILE_MENU][0], menu[FILE_MENU][1]))
        # break
    # else:
        # continue

# arquivo = menu[FILE_MENU][0]
# complement = menu[FILE_MENU][1]
# url = 'http://www.ons.org.br/resultados_operacao/SDRO/Diario/'
arquivo = '.\hist_hidraulicas.csv'
complement = '/geracao_arquivos/sheet002.htm'
url = 'http://www.ons.org.br/resultados_operacao/boletim_semanal/'

# Abre o histórico de geração e procura a última data com dados de medição
# with open(arquivo, newline='') as csvFile:
    # csvReader = csv.reader(csvFile, delimiter=';')
    # lastDate = list(csvReader)[-1][-0]
    # lastDate = datetime.datetime.strptime(lastDate, "%d/%m/%Y")
    # d1 = lastDate.date()
# csvFile.close()

# Procura no site do ONS as medições mais recentes
# reqDate = requests.get('http://www.ons.org.br/resultados_operacao/SDRO/Diario/topo.htm')
# reqDate.encoding = 'utf8'
# soupDate = bs4.BeautifulSoup(reqDate.text, "html.parser")
# textDate = soupDate.find_all('option')
# textDate = textDate[1].get_text()
# textDate = datetime.datetime.strptime(textDate[-10:], '%d/%m/%Y')
# d2 = textDate.date()

# Entrada de datas específicas para testes
d1 = datetime.date(2017, 1, 6)
d2 = datetime.date(2017, 6, 6)

# Número de dias entre o último registro local e o disponível no ONS
numDays = (d2 - d1).days
dataAtual = d1
dates = []

print('A última data de medições no arquivo local é: {}'.format(d1))
print('A última data de medições no site do ONS é: {}'.format(d2))


# Gerando datas para a url
while (d2-dataAtual).days > 0:
    dates.append((dataAtual).strftime("%Y_%m_%d"))
    dataAtual = dataAtual + datetime.timedelta(days=7)
    
# for i in range(0, numDays + 7):
    # dates.append((d1 + datetime.timedelta(days=i)).strftime("%Y_%m_%d"))

if (input('Importar útimas medições? (S/N) ').upper() == ('S')) and (numDays > 0):

    with open(arquivo, 'a', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=';')

        for date in dates:
            urlFull = url + date + complement
            res = requests.get(urlFull)

            if res.ok:
                # res.encoding = 'utf8'
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                text = soup.find_all('table')
                # A função anterior retorna um arry com todas as tabelas do frame
                # queremos a que contem os dados das usinas, supõe-se que seja a
                # maior.
                text = max(text, key=len)
                text = text.find_all('tr')

                # i = 0
                n = datetime.datetime.strptime(date, "%Y_%m_%d").date().strftime("%d/%m/%Y")

                for value in range(5, len(text) - 1):
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
    # tratar o cabeçalho
    # talvez importar os valores do find_all('tr')
