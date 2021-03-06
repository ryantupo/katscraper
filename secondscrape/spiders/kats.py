import scrapy
import mysql.connector
from secondscrape.database.db_connection import *;


class kats(scrapy.Spider):

    name = "kats"
    start_urls = ["https://www.pinterest.co.uk/joyishkennedy4/kit-kat-pics/"]


        


    def parse(self, response):
        
        image_links = []
        links = response.xpath("//img/@src")
        url_links = response.xpath("//a/@href")
        html = ""
        
        for url_link in url_links:
            url = url_link.get()
            
            if any(extension in url for extension in [".html", ".php"]):
                
                print ("External Link Found")
                add_link(url)
            else:
                add_link("https://www.pinterest.co.uk" + url)
                print ("Internal EndPoint Found", url)

        for link in links:
            url = link.get()

            if any(extension in url for extension in [".jpg", ".gif", ".png"]):

                html += """<a href="{url}"
                target="_blank"><img src="{url}"
                height="33%"
                width="33%"/><a/>""".format(url=url)

                add_image(url)
                
                log_data(html)

                image_links.append("{url}")
                
        # for link in return_link_list:
        #     yield response.follow(link.get(), callback=self.parse)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


