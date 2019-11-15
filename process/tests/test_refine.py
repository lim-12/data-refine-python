# -*- coding: utf-8 -*-
"""
    process.tests.test_refine
"""
import unittest

from process.refine import Refine


class TestRefine(unittest.TestCase):

    def make_refine(self, bundle_unit):
        return Refine(bundle_unit)

    def test_refine_text(self):
        """"""
        buf = """
                <HTML>
                    <BODY id ="123">
                        <p>he1ll4o wo6rl8d9</p>
                    </BODY>
                </HTML>
        """
        expected_buf = 'B1B1D2D3d4d6e8H9HhiLLlllMMOOoopprTTwYY'
        r = self.make_refine(7)
        # 실행
        buf = r.refine_text(buf)
        # 검증
        assert buf == expected_buf

    def test_obtain_result(self):
        """"""
        buf = 'd0E1e2h3l3l5l7O7o8o8R9rWw'
        expected_buf = {'quotient': 'd0E1e2h3l3l5l7O7o8o8R', 'remainder': '9rWw'}
        r = self.make_refine(7)
        # 실행
        buf = r.obtain_result(buf)
        # 검증
        assert buf == expected_buf