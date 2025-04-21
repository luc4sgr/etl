# Importing Scrapy module
# Importando o módulo Scrapy
import scrapy


# Definition of the spider class for scraping notebook data
# Definição da classe spider para raspagem de dados de notebooks
class NotebookSpider(scrapy.Spider):
    # Unique name used to run the spider
    # Nome único usado para executar o spider
    name = "notebook"

    # Allowed domains to avoid crawling external sites
    # Domínios permitidos para evitar raspagem de sites externos
    allowed_domains = ["lista.mercadolivre.com.br"]

    # Initial URL to start scraping
    # URL inicial para começar a raspagem
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]

    # Page tracking to limit pagination
    # Controle de páginas para limitar a paginação
    page_count = 1
    max_page = 10  # Maximum number of pages to scrape
                   # Número máximo de páginas a serem raspadas

    # Default callback function to process each response
    # Função de callback padrão para processar cada resposta
    def parse(self, response):
        # Select all product result containers
        # Seleciona todos os contêineres de resultado de produto
        products = response.css('div.ui-search-result__wrapper')

        # Loop through each product to extract data
        # Itera sobre cada produto para extrair os dados
        for product in products:
            # Extracts both original and discounted price values (if available)
            # Extrai os valores de preço original e com desconto (se disponíveis)
            prices = product.css('span.andes-money-amount__fraction::text').getall()

            # Yields a dictionary with the product data
            # Retorna um dicionário com os dados do produto
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),  # Brand name / Nome da marca
                'name': product.css('a.poly-component__title::text').get(),      # Product title / Título do produto
                'seller': product.css('span.poly-component__seller::text').get(),  # Seller name / Nome do vendedor
                'reviews_rating_number': product.css('span.poly-reviews__rating::text').get(),  # Rating / Avaliação
                'reviews_amount': product.css('span.poly-reviews__total::text').get(),  # Review count / Nº de avaliações
                'old_price': prices[0] if len(prices) > 0 else None,  # Original price / Preço original
                'new_price': prices[1] if len(prices) > 1 else None   # Discounted price / Preço com desconto
            }

        # Pagination control logic
        # Lógica de controle de paginação
        if self.page_count < self.max_page:
            # Extracts the next page link
            # Extrai o link da próxima página
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()

            # If there's a next page, schedule it for scraping
            # Se houver próxima página, agenda nova raspagem
            if next_page:
                self.page_count += 1  # Increment page count / Incrementa contador de páginas
                yield scrapy.Request(url=next_page, callback=self.parse)  # Recursive request / Requisição recursiva
