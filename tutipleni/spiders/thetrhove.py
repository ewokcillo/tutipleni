# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import os

from scrapy import Request, Spider

from tutipleni.settings import FILES_STORE


class ThetrhoveSpider(Spider):
    name = 'thetrhove'

    def start_requests(self):
        url = 'https://thetrove.net/Books'
        yield Request(url, self.parse_links)

    def parse_links(self, response):
        self.logger.info('Inspecting %s', response.url)
        dirs_links = response.xpath('//tr[@class="litem dir"]/td/a/@href')

        for link in dirs_links:
            link_str = link.get()
            if link_str != '../index.html':
                yield response.follow(response.url + link_str, self.parse_links)

        files_links = response.xpath('//tr[@class="litem file"]/td/a/@href')
        for file_link in files_links:
            request_url = response.url + file_link.get()[2:]
            request_path = urlparse(request_url).path
            file_path = FILES_STORE+request_path
            if not os.path.exists(file_path):
                yield Request(request_url, callback=self.parse_file,
                              cb_kwargs=dict(file_path=file_path))

    def parse_file(self, response, file_path):
        self.logger.info('Downloading %s', response.url)
        path = file_path[:file_path.rfind('/')]
        try:
            os.makedirs(path)
        except Exception:
            pass
        with open(file_path, 'wb') as f:
            f.write(response.body)
