import scrapy


class BnuScholarshipSpider(scrapy.Spider):
    name = 'bnu_scholarship'
    start_urls = ['https://www.bnu.edu.pk/bnu/Admissions/Fee-Scholarship']

    def parse(self, response):
        name='BNU'
        title=response.css('title::text').extract()

        address= response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "large-6", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "footer-text", " " ))]').get()
        scholarship_heading=response.css('h2::text').extract()
        scholarship_heading=response.css('h2:nth-child(4)::text , h2:nth-child(9)::text , h2~ p+ h2::text').extract()
        yield {'scholarship': scholarship_heading}
        yield {'address': address}
        yield {'title': title}
