import scrapy
from scrapy import Request
from WebCrawler.items import MyanimelistItem


class MyanimelistSpider(scrapy.Spider):
    name = 'myanimelist'
    allowed_domains = ['www.myanimelist.net']
    letters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    #Liste des pages à collecter
    start_urls = [f'https://myanimelist.net/manga.php?letter={letter}' for letter in letters]


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_manga)
        
        
    def parse_manga(self, response):
        liste_anime =  response.css('tr')
        
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for anime in liste_anime:
            item = MyanimelistItem()

            # Nom du film
            try:
                item['nom'] = anime.css('strong::text').extract()
            except:
                item['nom'] = 'None'
              
            # Lien de l'image du film
            try:
                item['img'] = anime.css(' img').attrib['data-src']
            except:
                item['img'] = 'None'


            # Auteur du film
            try:
                item['desc'] = anime.css(' div.pt4::text').extract()
            except:
                item['desc'] = 'None'
           


            yield item
