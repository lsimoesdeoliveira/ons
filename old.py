import requests
import bs4
import datetime
import time

   
d1 = datetime.date(2015, 6, 2)
d2 = datetime.date(2016, 12, 31)
delta = d2 - d1
data = []
for i in range(delta.days+1):
    data.append((d1 + datetime.timedelta(days=i)).strftime("%Y_%m_%d"))

url = 'http://www.ons.org.br/resultados_operacao/boletim_diario/'
fonteGeracaoUrl = '/geracao_arquivos/sheet003.htm'

for n in data:
    urlCompleta = url + n + fonteGeracaoUrl
    res = requests.get(urlCompleta)

    #res.encoding = 'utf8'

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    text = soup.find_all('tr')
    #break
    
    with open('D:\\Users\\lucas\\Documents\\Python\\ons\\hist2.txt', 'a') as f:
            
        for value in text:
            linha = value.get_text().strip().replace(' \n',';').replace('\n',';')
            linha = linha.split(';')
            linha = list(filter(bool, linha)) 
            if len(linha) == 4 and linha[0] != 'Submercado':
                f.write(n.replace('_','/') + ';' + linha[0] + ';' + linha[1] + '\n')
                print(linha)

    f.close()
    time.sleep(1.5)


#tratar o cabeçalho
#talvez importar os valores do find_all('tr')



