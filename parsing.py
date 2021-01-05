import csv 
import datetime
import requests
from bs4 import BeautifulSoup

main_url = "http://kenesh.kg/ru/deputy/list/35"

def get_html(url):
    res = requests.get(url)
    # print(res)  #print(res) ---> poluchim HTML code
    return res.text

def get_all_links(html):    #vozvrashaet return res.text
    soup = BeautifulSoup(html, 'html.parser')
    # print("MY SOUP", soup)
    tds = soup.find('table', class_ = 'table').find_all('td')
    # print(tds)
    # tds = set(tds)
    links = []

    for td in tds:	
        catched_url = td.find('a').get('href')
        if catched_url.startswith('/ru/deputy/'):
            link = 'http://kenesh.kg' + catched_url
            if link not in links:
                links.append(link)
        # print(link)
    return links

    '''We are getting their numbers and names'''

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('h3', class_ = 'deputy-name').text.strip()
    except:
        name = ''
    try	
        number = soup.find('p', class_ = 'mb-10').find('a').get('href')
    except:
        number = ''
    data = {'name': name, 'number': number}
    return data

def write_csv(data):
    with open('deputy.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['number']])
        print([data['name'], data['number']], 'parsed')




def main():
    start = datetime.datetime.now()
    html_text = get_html(main_url)
    all_links = get_all_links(html_text)
    for link in all_links:
        # print(link)
        # get_html(link)
        html = get_html(link)
        data = get_page_data(html)
        write_csv(data)
    end = datetime.datetime.now()
    res = end - start
    print(str(res))

# def main():
#     get_html(main_url)

if __name__ == '__main__':
    main()







