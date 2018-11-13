# -*- coding: utf-8 -*-

import re


def decodeJsFuncs(str, key, value):
    pos = str.index("var")
    if pos > 0:
        str = str[:pos]
    key = str.split("()")[0]
    key = key.replace('function', '')
    key = key.strip()
    if str.endswith('function'):
        str = str.rstrip('function')
    str = str.strip()



def getAutohomeDict(js, dict_slice):
    map_strs = {}
    dict_slice = {}
    map_source = {}
    str = js.replace("})(document);</script>", "function")
    pattren = 'function\s(\S){0,2}_\(\)\s*\{.*?\}+\s+'
    re_comp = re.compile(pattren)
    matches = re.findall(re_comp)
    for fc in matches:
        key, value = decodeJsFunc(fc)
