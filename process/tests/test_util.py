# -*- coding: utf-8 -*-
"""
    process.tests.test_util
"""
import unittest

from process.util import quick_sort, cross_combine, remove_tag


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        buf = ['H', 'e', 'l', 'L', 'o', 'W', 'o', 'R', 'L', 'D']
        expected_buf = ['D', 'e', 'H', 'L', 'L', 'l', 'o', 'o', 'R', 'W']
        # 실행
        buf = quick_sort(buf)
        # 검증
        assert buf == expected_buf


class TestCrossCombine(unittest.TestCase):

    def test_cross_combine(self):
        # after list 크기가 더 큰 경우
        buf1 = ['D', 'e', 'H', 'L', 'L', 'l', 'o', 'o', 'R', 'W']
        buf2 = ['0', '0', '1', '1', '1', '4', '4', '6', '6', '6', '6', '9', '9', '9', '9']
        # after list와 before list 크기가 동일한 경우
        buf3 = ['D', 'e', 'H', 'L', 'L', 'l', 'o', 'o', 'R', 'W']
        buf4 = ['0', '0', '1', '1', '1', '4', '4', '6', '6', '6']
        # after list 크기가 더 작은 경우
        buf5 = ['D', 'e', 'H', 'L', 'L', 'l', 'o', 'o', 'R', 'W']
        buf6 = ['0', '0', '1', '1', '1', '4']
        expected_buf1 = 'D0e0H1L1L1l4o4o6R6W669999'
        expected_buf2 = 'D0e0H1L1L1l4o4o6R6W6'
        expected_buf3 = 'D0e0H1L1L1l4ooRW'

        # 실행
        r1 = cross_combine(buf1, buf2)
        r2 = cross_combine(buf3, buf4)
        r3 = cross_combine(buf5, buf6)
        # 검증
        assert r1 == expected_buf1
        assert r2 == expected_buf2
        assert r3 == expected_buf3


class TestRemoveTag(unittest.TestCase):

    def test_remove_tag(self):
        buf = '<HTML><BODY id="123"><p>he1ll4o wo6rl8d9</p></BODY></HTML>'
        expected_buf = 'he1ll4o wo6rl8d9'
        # 실행
        buf = remove_tag(buf)
        # 검증
        assert buf == expected_buf
