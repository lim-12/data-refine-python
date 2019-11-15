# -*- coding: utf-8 -*-
"""
    process.util
"""
import re


def quick_sort(arr):
    """
    :param arr: 배열
    :return: 배열 안에 데이터를 정렬한 배열
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)/2]
    lesser, equal, greater = [], [], []
    for value in arr:
        """
        upper()를 사용하지 않을 경우, 문자(영어)의 경우 아스키코드 값 기준으로 정렬되기 때문에
        upper()를 사용하여 대소문자를 구분하지 않고 정렬한다.
        정렬을 할 때에는 upper()를 사용하여 모두 대문자로 변경하여 비교하지만 실제 값은 원본 데이터를 입력한다.
        """
        if value.upper() < pivot.upper():
            lesser.append(value)
        elif value.upper() > pivot.upper():
            greater.append(value)
        else:
            equal.append(value)
    """
    정렬이 완료된 이후에 equal 배열에 있는 데이터를 정렬해준다.
    upper()를 사용하여 비교 후, 원본데이터를 입력했기 때문에 동일한 알파벳에 대해 대문자와 소문자가 섞여있기 때문이다.
    ex) equal = ['a', 'A', 'a', 'a', 'A'] > sorted(equal) = ['A', 'A', 'a', 'a', 'a']
    """
    return quick_sort(lesser) + sorted(equal) + quick_sort(greater)


def cross_combine(before, after):
    """
    :param before: 교차시 우선 교차 시킬 list
    :param after: 교차시 후순위 교차 시킬 list
    :return: list를 교차한 값
    """
    result = ""

    before_len = len(before) - 1
    for (idx, v) in enumerate(before):
        try:
            result += v + after[idx]
        except IndexError:
            # before list의 크기가 더 클 경우, after list IndexError 발생
            result += ''.join(before[idx:])
            break
        if idx == before_len:
            try:
                result += ''.join(after[idx+1:])
            except IndexError:
                # before list의 크기와 after list의 크기가 동일할 경우 IndexError 발생
                pass
    return result


def remove_tag(html):
    """
    :param html: 문자 
    :return: html 태그가 제거된 문자
    """
    tag_removed_html = re.sub('<(/)?([a-zA-Z]*)(\\s[a-zA-Z]*=[^>]*)?(\\s)*(/)?>', '', html)

    return tag_removed_html
