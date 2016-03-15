from django.core.management.base import BaseCommand
from bereken.models import Leveranciers, Kosten
import webbrowser, sys, time, requests, bs4,re

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        tlisp = Tag(name='Lisp')
        tlisp.save()

        tjava = Tag(name='Java')
        tjava.save()

    def handle(self, *args, **options):
        self._create_tags()

    def create_url():
	nuon='https://www.gaslicht.com/energie-vergelijken/nuon/vasteprijsstroom-plus-gas-tot-1-jr?pcnum=2406&pcalpha=AL&housenr=14&stroomhoogverbruik=700&gasverbruik=700&rows=153#tab-prijsdetail'+e1.get()
	eneco='https://www.gaslicht.com/energie-vergelijken/eneco/ecostroom-plus-aardgas-voordeel-1-jr-vast-actie?pcnum=2406&pcalpha=AL&housenr=14&stroomhoogverbruik=700&gasverbruik=700#tab-prijsdetail'+e1.get()
	urls=[beslist_url,tweakers_url,amazon_url]
    return(urls)

    def get_prices():
	urls=create_url()
   	i=0
	for u in urls:
        	r = requests.get(u, "headers=headers")
        	r.raise_for_status()
        	web = bs4.BeautifulSoup(r.text,"html.parser")
        	if i==0:#nuon
           		price=web.find_all('div',{'class':'contentCol noteText'})[1].text
        	elif i==1:#eneco
            		price=web.find_all('div',{'class':'contentCol noteText'})[1].text
        	i=i+1
    	return()
