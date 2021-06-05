import scrapy
import mysql.connector


class kats(scrapy.Spider):
    


    name = "kats"
    start_urls = ["https://www.pinterest.co.uk/joyishkennedy4/kit-kat-pics/"]

    def parse(self, response):
        image_links = []
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()

            if any(extension in url for extension in [".jpg", ".gif", ".png"]):
            
                if "{url}" not in image_links:
                    html += """<a href="{url}"
                    target="_blank"><img src="{url}"
                    height="33%"
                    width="33%"/><a/>""".format(url=url)

                    with open("frontpage.html", "a") as page:
                        page.write(html)
                        page.close()
                    

                    with open("frontpage.json", "a") as page:
                        page.write(html)
                        page.close()
                    
                    image_links.append("{url}")
            
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
