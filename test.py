# -*- coding: utf-8 -*-

import re


def decodeJsFuncs(str, key, value):
    pos = str.index("var")
    if pos > 0:
        str = str[:pos]
    key = str.split("()")[0]
    key = key.replace("function", "", -1)
    key = key.strip()

    if str.endswith("function"):
        str = str.strip("function")
    str = str.strip()


def getAutoHomeDict(js, dict_slice):
    matches = []
    str = re.match(js, "})(document);</script>", " function", -1)
    pattern = '''function\s(\S){0,2}_\(\)\s*\{.*?\}+\s+'''
    re_comp = re.compile(pattern)
    matches = re_comp[str:-1]

