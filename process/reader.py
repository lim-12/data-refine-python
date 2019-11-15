# -*- coding: utf-8 -*-
"""
    process.reader
"""
import requests


class Reader:
    """
    데이터를 읽어오는 클래스
    """
    def __init__(self, url):
        self.__url = url

    def read(self):
        return requests.get(self.__url).text
