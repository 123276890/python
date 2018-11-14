# -*- coding: utf-8 -*-

import re


def decodeJsFuncs(string):
    try:
        pos = string.index("var")
    except ValueError:
        pos = -1
    if pos > 0:
        string = string[:pos]
    key = string.split("()")[0]
    key = key.replace('function', '')
    key = key.strip()
    if string.endswith('function'):
        string = string.rstrip('function')
    string = string.strip()
    if len(re.compile(r'function').findall(string)) > 1:
        try:
            function_name = re.search(r'''
                    function\s+(\w+)\(\)\s*\{\s*
                        function\s+\w+\(\)\s*\{\s*
                            return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                        \};\s*
                        if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                            return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                        \}\s*else\s*\{\s*
                            return\s*\w+\(\);\s*
                        \}\s*
                    \}
                    ''', string, re.X)
            a, b, c, d = function_name.groups()
            value = d if b == c else b
            return key, value
        except:
            function_name = re.search(r'''
                    function\s+(\w+)\(\)\s*\{\s*
                        function\s+\w+\(\)\s*\{\s*
                            return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                        \};\s*
                        if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                            return\s*\w+\(\);\s*
                        \}\s*else\s*\{\s*
                            return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                        \}\s*
                    \}
                    ''', string, re.X)
            a, b, c, d = function_name.groups()
            value = b if b == c else d
            return key, value
    else:
        function_name = re.search(r'''
            function\s*(\w+)\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        ''', string, re.X)
        a, b = function_name.groups()
        value = b
        return key, value


def decodeJsVars(string):
    string = string.replace('var', '')
    string = string.strip()
    if string.count("=") > 0:
        pair = string.split("=", 2)
        key = pair[0].strip()
        value = pair[1].strip()
        value = value.strip("'")
        return key, value


def decodeJsVarfuncs(string):
    string = string.replace("var", "")
    string = string.strip()
    if string.count("=") > 0:
        pair = string.split("=", 2)
        key = pair[0]
        if pair[1].count("function") > 0:
            if len(re.compile(r'function').findall(string)) > 1:
                function_name = re.search(r'''
                            [A-z]{0,2}_=function\(\)\{\'\S{0,2}_\';\s*
                                \s_\w=function\(\)\{return\s*[\'\"]([^\'\"]+)[\'\"];\};\s*
                                return\s*_[A-z]\(\);\}\s*
                            ''', string, re.X)
                a = function_name.group(1)
                value = a
                return key, value
            else:
                function_name = re.search(r'''
                             [A-z]{0,2}_=function\(\)\s*\{\s*
                                [\'\"]return\s*[A-z]{0,2}_+[\'\"];\s*
                                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                                \}\s*
                        ''', string, re.X)
                a = function_name.group(1)
                value = a
                return key, value


def getAutoHomeDict(js):
    map_strs = {}
    dict_slice = {}
    map_source = {}
    string = js.replace("})(document);</script>", "function")
    matches = re.compile(r"function\s\S\S_\(\)\s*\{.*?\}+\s+").findall(js)                                  # 匹配 function
    for fc in matches:
        key, value = decodeJsFuncs(fc)
        map_source[key] = fc
        if key != '':
            map_strs[key] = value
    matches = re.compile(r"var\s?\S\S_=\s?'\S*'").findall(string)                                           # 匹配var申明
    for variable in matches:
        key, value = decodeJsVars(variable)
        map_source[key] = variable
        if key != '':
            map_strs[key] = value
    matches = re.compile(r"var\s?\S\S_=\s?function\s?\(\)\s?\{.*?return.*?return.*?\}").findall(string)      # 匹配 var functions
    for varfunc in matches:
        key, value = decodeJsVarfuncs(varfunc)
        map_source[key] = varfunc
        if key != "":
            map_strs[key] = value
    print(map_strs)

