import requests
from bs4 import BeautifulSoup
import csv


# Функция для парсинга данных с сайта rlisystems.ru
def parse_rlisystems():
    with open('table_INN.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Наименование', 'ИНН', 'Наличие ЭЦП', 'Ссылка'])
    url = 'https://www.rlisystems.ru/info/operinfo/clients/RolisClients.php'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    file = open('table_INN.csv', 'a', encoding='utf-8-sig', newline='')
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        company_name = cells[0].text.strip()
        link = cells[0].find('a')
        if link:
            link = link.get('href')
        else:
            link = 'нет ссылки'
        print(link)
        inn = cells[1].text.strip()
        ecp = cells[2].text.strip()
        
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
                company_name, inn, ecp, link,
            ])

    file.close()
    print('Файл создан')
# Функция для парсинга данных с ati.su

# Вызываем функцию для парсинга данных с rlisystems.ru
parse_rlisystems()
