from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl
from django.http import HttpResponse, JsonResponse


# Create your views here.
def get_curruency(request):
    req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
    # opening site and read it's html
    context = ssl._create_unverified_context()
    html = urlopen(req, context=context).read()
    have = dict()
    # using beatifulSoap for parsing data in html
    bs = BeautifulSoup(html, 'html.parser')
    # Find first 5 table rows
    rows = bs.find('tbody', class_="table__body").find_all('tr', class_="table__row")
    for row in rows:
        try:
            cryptocurrency = row.find('span', class_="profile__name").get_text().strip().replace('\n', '')
            values = row.find_all('div', class_="valuta")
            price = values[0].get_text().strip().replace('\n', '')
            cryptocurrency = ' '.join(cryptocurrency.split())
            price = ' '.join(price.split())
            price = price.replace('$', '').replace(',', '').replace(' ', '')
            have[cryptocurrency] = float(price)
            print(cryptocurrency)
        except Exception as e:
            print(e)
    data = {
        'rate': have['Ethereum ETH'],
        'rate_classic': have['Ethereum Classic ETC']
    }
    return render(request, 'index.html', data)
