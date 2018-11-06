# -*- coding: utf-8 -*-

import re

def decodeJsFuncs(str, key, value):
    

def getAutoHomeDict(js, dict_slice):
    matches = []
    str = re.match(js, "})(document);</script>", " function", -1)
    pattern = '''function\s(\S){0,2}_\(\)\s*\{.*?\}+\s+'''
    re_comp = re.compile(pattern)
    matches = re_comp[str:-1]
    for key, fc in matches:
        value =
