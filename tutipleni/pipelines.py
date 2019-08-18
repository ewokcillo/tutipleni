# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline
from tutipleni.settings import FILES_STORE


class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response, info):
        path = urlparse(response.url).path
        try:
            os.makedirs(FILES_STORE+path[:path.rfind('/')])
        except Exception:
            self.logger.info('Path exists %s', path)
        return path


class TutipleniPipeline(object):
    def process_item(self, item, spider):
        return item
