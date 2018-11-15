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
    dic = ""
    string = js.replace("})(document);</script>", "function")
    matches = re.compile(r"function\s\S\S_\(\)\s*\{.*?\}+\s+").findall(js)                                  # 匹配function
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
    matches = re.compile(r"var\s?\S\S_=\s?function\s?\(\)\s?\{.*?return.*?return.*?\}").findall(string)      # 匹配var和functions
    for varfunc in matches:
        key, value = decodeJsVarfuncs(varfunc)
        map_source[key] = varfunc
        if key != "":
            map_strs[key] = value
    pattren = re.compile(r"function\s*\$FillDicData\$\s*\(\)\s*?{.*?\$RenderToHTML")                         # 拼接字典
    is_match = pattren.search(js)
    if is_match != None:
        str_match = str(pattren.findall(js))

        if str_match.find("$GetWindow$()") == -1:
            pass
        position = str_match.index("$GetWindow$()")
        str_tmp = str_match[position:]

        if str_match.find("$rulePosList$") == -1:
            pass
        position = str_match.index("$rulePosList$")
        str_tmp = str_match[:position]

        if str_match.find("]") == -1:
            pass
        position = str_match.index("]")
        str_tmp = str_tmp[position + 1:]
        strs_dict = str_tmp.split("+")

        i = 1
        while i < len(strs_dict):
            str_to_match = strs_dict[i]
            is_match = re.compile(r"\(\'\S+\'\)").search(str_to_match)

            if is_match != None:
                tmp = re.compile(r"\(\'\S+\'\)").findall(str_to_match)[0]
                tmp = tmp.replace("(", "")
                tmp = tmp.replace(")", "")
                tmp = tmp.replace("'", "")
                tmp = tmp.strip()
                dic += tmp

            elif re.compile(r"^\'\S+\'$").search(str_to_match) != None:
                tmp = str_to_match.replace("'", "")
                tmp = tmp.strip()
                dic += tmp

            elif re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").search(str_to_match) != None:
                str_matched = re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").match(str_to_match)

                if re.compile(r"return\s?\'\S+\'").search(str(str_matched)) != None:
                    str_tmp = re.compile(r"return\s?\'\S+\'").findall(str(str_matched))[0]

                    tmp = str_tmp.replace("return", "")
                    tmp = tmp.replace("'", "")
                    tmp = tmp.strip()
                    dic += tmp

            elif re.compile(r"^\S{2}_\(\)$").search(str_to_match) != None:
                key = str_to_match.replace("()", "")
                tmp = map_strs[key]
                dic += tmp

            elif re.compile(r"^\S{2}_$").search(str_to_match) != None:
                key = str_to_match
                dic += map_strs[key]

            elif re.compile(r"\('([A-Z]|[a-z]|[0-9]|[,]|[']|[;]|[\u4e00-\u9fbb]){1,10}'\)").search(str_to_match) != None:
                tmp = re.compile(r"\('([A-Z]|[a-z]|[0-9]|[,]|[']|[;]|[\u4e00-\u9fbb]){1,10}'\)").match(str_to_match)
                if len(tmp) >= 2:
                    tmp = tmp[:2]
                dic += tmp

            else:
                dic += "X"

            i += 1

    indexes = ""                                                                                             # 拼接字符串
    position = str_match.find("$rulePosList$")
    str_tmp = str_match[position:]

    position = str_tmp.find("$SystemFunction2$")
    str_tmp = str_tmp[:position - 2]
    str_tmp = str_tmp.strip()
    strs_indexes = str_tmp.split("+")
    i = 1
    while i < len(strs_indexes):
        str_to_match = strs_indexes[i]
        tmp = ""

        if re.compile(r"\(\'\S+\'\)").search(str(str_to_match)) != None:
            tmp = re.compile(r"\(\'\S+\'\)").findall(str_to_match)
            tmp = str(tmp).replace("(", "")
            tmp = tmp.replace(")", "")
            tmp = tmp.replace("'", "")
            tmp = tmp.strip()
            tmp = tmp.strip("[")
            tmp = tmp.strip("]")
            tmp = tmp.strip('"')
            indexes += tmp

        elif re.compile(r"^\'\S+\'$").search(str(str_to_match)) != None:
            tmp = str_to_match.replace("'", "")
            tmp = tmp.strip()
            indexes += tmp

        elif re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").search(str(str_to_match)) != None:
            str_matched = re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").findall(str_to_match)

            if re.compile(r"return\s?\'\S+\'").search(str(str_to_match)) != None:
                str_tmp = re.compile(r"return\s?\'\S+\'").findall(str(str_matched))

                tmp = str(str_tmp).replace("return", "")
                tmp = tmp.replace("'", "")
                tmp = tmp.strip()
                tmp = tmp.strip("[")
                tmp = tmp.strip("]")
                tmp = tmp.strip('"')
                indexes += tmp

        elif re.compile(r"^\S{2}_\(\)$").search(str(str_to_match)) != None:
            key = str_to_match.replace("()", "")
            tmp = map_strs[key]
            indexes += tmp

        elif re.compile(r"^\S{2}_$").search(str(str_to_match)) != None:
            key = str_to_match
            tmp = map_strs[key]
            indexes += tmp

        elif str_to_match.strip() == "''":
            i += 1
            continue

        else:
            indexes += "X"

        i += 1

    runes_dic = []
    for d in dic:
        d = ord(d)
        runes_dic.append(d)
    items = indexes.split(";")
    for i, string in enumerate(items):
        sbresult = ""
        if string =="":
            continue
        nums = string.split(",")
        for num in nums:
            try:
                index = int(num)
            except:
                continue

            if index < len(runes_dic):
                s = chr(runes_dic[index])
                sbresult += s

        dict_slice[i] = sbresult

    # return






