import scrapy
from scrapy import Request
from WebCrawler.items import BoursoramaItem #Importe la class contenant vos items (champs collectés) ==> à compléter
import time
from datetime import datetime as d

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com']
    start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}' for n in range(1,10)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indices in liste_indices:
            item = BoursoramaItem()#importer la class Items du projet provenant du fichier items.py
            
            #indice boursier
            try: 
              item['indice'] = indices.css('a.c-link::text').extract()
            except:
              item['indice'] = 'None'
            
            #indice cours de l'action
            try: 
              item['cours'] = indices.css('span.c-instrument.c-instrument--last::text').extract()
            except:item['cours'] = 'None'
            
            #Variation de l'action
            try: 
              item['var'] =indices.css('span.c-instrument.c-instrument--instant-variation::text').extract() #à compléter
            except:
              item['var'] = 'None'
            
            #Valeur la plus haute
            try: 
              item['hight'] = indices.css('span.c-instrument.c-instrument--high::text').extract()#à compléter
            except:
              item['hight'] = 'None'
            
            #Valeur la plus basse
            try: 
              item['low'] = indices.css('span.c-instrument.c-instrument--low::text').extract()#à compléter
            except:
              item['low'] = 'None'

            #Valeur d'ouverture
            try: 
              item['open_'] = indices.css('span.c-instrument.c-instrument--open::text').extract()#à compléter
            except:
              item['open_'] = 'None'

            #Date de la collecte
            try: 
              item['time'] = d.now()
            except:
              item['time'] = 'None'

            
            yield item