# -*- coding: utf-8 -*-
"""
    process.refine
"""
import re
import util


class Refine:
    """
    데이터를 정제하는 클래스
    """
    def __init__(self, bundle_unit):
        self.__bundle_unit = bundle_unit

    def refine_text(self, text):
        """
        :param text: 문자
        :return: 입력된 문자 중 숫자와 영문이 아닌 문자를 제거한 후, 숫자와 영문을 교차한 값
        """
        return util.cross_combine(
                util.quick_sort(re.sub('[^a-zA-Z]', '', text)),
                sorted(re.sub('[^0-9]', '', text)))

    def obtain_result(self, text):
        """
        :param text: 문자 
        :return: 묶음 단위로 계산 된 몫과 나머지
        """
        point = len(text) - len(text) % self.__bundle_unit
        return {'quotient': text[:point], 'remainder': text[point:]}