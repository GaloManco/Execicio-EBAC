# Meu primeiro execicio no github
print('Olá Mundo!!!')

# Nesse execicio da ebac vou subir um codigo de um webscrapy do site IMDB
# salvando todos os top 100 melhores filmes desse site e tudo salvo 
# em um lista em um arquivo.csv.

import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'

    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_nv250']

    def parse(self, response):
        for filmes  in response.css('.titleColumn'):
            yield {
                  'titulo': filmes.css('.titleColumn a::text').get(),
                  'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                  'nota': response.css('strong ::text').get()
            }
        pass
