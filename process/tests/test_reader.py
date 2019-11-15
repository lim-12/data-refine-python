# -*- coding: utf-8 -*-
"""
    process.tests.test_reader
"""
import unittest

from process.reader import Reader


class TestReader(unittest.TestCase):

    def make_reader(self, url):
        return Reader(url)

    def test_read(self):
        """EP 읽기 테스트"""
        url = 'https://www.w3schools.com/xml/note.xml'
        # 원본 데이터를 미리 만들어 둔 텍스트
        expected_buf = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n"
                        "<note>\r\n"
                        "  <to>Tove</to>\r\n"
                        "  <from>Jani</from>\r\n"
                        "  <heading>Reminder</heading>\r\n"
                        "  <body>Don't forget me this weekend!</body>\r\n"
                        "</note>")

        r = self.make_reader(url)
        # 실행
        buf = r.read()
        # 검증
        assert buf == expected_buf
