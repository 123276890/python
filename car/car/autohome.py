# -*- coding: utf-8 -*-

import re
import json
from .items import CarItem


# 循环抓取数据
def GraspTheData(v, path, ret, key, dic):
    for value in v[path]:
        dealAutoHomeItemValue(value, ret, key, dic)


def NewAutoHomeCar(aid):
    c = CarItem()
    c['settings'] = "https://car.autohome.com.cn/config/spec/" + str(aid) + ".html"
    return c


def fetchCarInfo(html):
    car_info_datas = re.compile(r"<script>((?:.|\\n)*?)</script>").findall(html)
    js_matches = []
    dic = {}

    for strs in car_info_datas:
        strslist = []
        for s in strs:
            s = ord(s)
            strslist.append(s)
        if strs.find("try{document.") < 0:
            if len(strslist) > 500:
                js_matches.append(strs)

    for i, js in enumerate(js_matches):
        if i == 1:
            dic["config"] = getAutoHomeDict(js)
        elif i == 2:
            dic["option"] = getAutoHomeDict(js)
        else:
            pass

    # 基本参数组
    pos_start = html.find("var config =")
    if pos_start <= 0:
        pass
    str_base = html[pos_start:]
    pos_end = str_base.find('''\n''')
    if pos_end > len(str_base):
        pass
    str_base = str_base[13:pos_end - 1]

    # 选项配置参数组
    pos_start = html.find("var option =")
    if pos_start <= 0:
        pass
    str_option = html[pos_start:]
    pos_end = str_option.find('''\n''')
    if pos_end > len(str_option):
        pass
    str_option = str_option[13:pos_end - 1]

    # 外观颜色json
    pos_start = html.find("var color =")
    if pos_start <= 0:
        pass
    str_color = html[pos_start:]
    pos_end = str_color.find('''\n''')
    if pos_end > len(str_color):
        pass
    str_color = str_color[12:pos_end - 1]

    # 内饰颜色Json
    pos_start = html.find("var innerColor =")
    if pos_start <= 0:
        pass
    str_inner = html[pos_start:]
    pos_end = str_inner.find('''\n''')
    if pos_end > len(str_inner):
        pass
    str_inner = str_inner[16:pos_end - 1]

    # 车型ID抓取
    result = json.loads(str_base)["result"]["speclist"]
    ret = {}
    if type(result) != None and len(result) != 0:
        items = list(result)
        for item in items:
            key_car_id = item["specid"]
            if key_car_id != None and len(str(key_car_id)) != 0:
                car_id = int(key_car_id)
                car = NewAutoHomeCar(car_id)
                ret[car_id] = car

    # 基本参数抓取
    result = json.loads(str_base)["result"]["paramtypeitems"]
    if type(result) != None and len(result) != 0:
        items = list(result)
        for item in items:
            item_name = str(item["name"])

            if item_name == "基本参数":
                base_params = list(item["paramitems"])

                for v in base_params:
                    name = str(v["name"])
                    # 能源类型
                    if name.count("能源类型") > 0:
                        GraspTheData(v, "valueitems", ret, "energy_type_str", dic)
                    # 上市时间
                    if name.count("上市") > 0:
                        GraspTheData(v, "valueitems", ret, "market_time", dic)
                    # 工信部纯电续航里程
                    if name.count(("工信部纯电续航里程")) > 0:
                        GraspTheData(v, "valueitems", ret, "e_mileage", dic)
                    # 变速箱
                    if name.count(("变速箱")) > 0:
                        GraspTheData(v, "valueitems", ret, "gearbox", dic)

                    id = int(v["id"])
                    # 级别
                    if id == 220:
                        GraspTheData(v, "valueitems", ret, "car_level_str", dic)
                    # 车型名称
                    elif id == 567:
                        GraspTheData(v, "valueitems", ret, "car_name", dic)
                    # 最大功率
                    elif id == 295:
                        GraspTheData(v, "valueitems", ret, "max_power", dic)
                    # 最大扭矩
                    elif id == 571:
                        GraspTheData(v, "valueitems", ret, "max_torque", dic)
                    # 发动机
                    elif id == 555:
                        GraspTheData(v, "valueitems", ret, "engine", dic)
                    # 长*宽*高
                    elif id == 222:
                        GraspTheData(v, "valueitems", ret, "car_size", dic)
                    # 车身结构
                    elif id == 281:
                        GraspTheData(v, "valueitems", ret, "car_struct", dic)
                    # 最高车速
                    elif id == 267:
                        GraspTheData(v, "valueitems", ret, "max_speed", dic)
                    # 官方100加速
                    elif id == 225:
                        GraspTheData(v, "valueitems", ret, "official_speedup", dic)
                    # 实测100加速
                    elif id == 272:
                        GraspTheData(v, "valueitems", ret, "actual_speedup", dic)
                    # 实测100制动
                    elif id == 273:
                        GraspTheData(v, "valueitems", ret, "actual_brake", dic)
                    # 工信部综合油耗
                    elif id == 271:
                        GraspTheData(v, "valueitems", ret, "gerenal_fueluse", dic)
                    # 实测油耗
                    elif id == 243:
                        GraspTheData(v, "valueitems", ret, "actual_fueluse", dic)
                    # 整车质保
                    elif id == 274:
                        GraspTheData(v, "valueitems", ret, "quality_guarantee", dic)
                    else:
                        pass

            if item_name == "车身":
                body_params = list(item["paramitems"])

                for v in body_params:
                    id = int(v["id"])

                    # 长度(mm)
                    if id == 275:
                        GraspTheData(v, "valueitems", ret, "length", dic)
                    # 宽度(mm)
                    elif id == 276:
                        GraspTheData(v, "valueitems", ret, "width", dic)
                    # 高度(mm)
                    elif id == 277:
                        GraspTheData(v, "valueitems", ret, "height", dic)
                    # 轴距(mm)
                    elif id == 132:
                        GraspTheData(v, "valueitems", ret, "shaft_distance", dic)
                    # 前轮距(mm)
                    elif id == 278:
                        GraspTheData(v, "valueitems", ret, "front_wheels_gap", dic)
                    else:
                        pass


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


def replaceDashAsNullString(s):
    if s.count("&nbsp;") > 0:
        s = s.replace("&nbsp;", "")
    return s


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

    return dict_slice


def replaceHtmlByDict(origin, dic):
    value = origin
    if re.compile(r"<span class='hs_kw.*?'></span>").search(origin) != None:
        str_matches = re.compile(r"<span class='hs_kw.*?'></span>").findall(origin)

        for str in str_matches:
            tmp = str.replace("<span class='hs_kw", "")
            tmp = tmp.replace("></span>", "")

            str_num = re.compile(r"\d*").findall(tmp)
            num = int(str_num[0])

            if tmp.count("config") > 0:
                if num < len(dic["config"]):
                    str_to_replace = dic["config"][num]
                    value = value.replace(str, str_to_replace)
                elif tmp.count("option") > 0:
                    if num < len(dic["option"]):
                        str_to_replace = dic["option"][num]
                        value = value.replace(str,str_to_replace)
                elif tmp.count("keyLink") > 0:
                    value = str(dic["keyLink"][num])
        return value


def dealAutoHomeItemValue(item, info = {}, key = "", dic = {}):
    id = item["specid"]
    if not(type(id) != None and len(str(id)) != 0):
        return
    car_id = int(id)
    try:
        car = info[car_id]
    except:
        pass
    value = str(item["value"])
    if key == "Car_type":
        value = 1
    if key == "Engine_type":
        value = car["engine"]
    if value != "":
        value = replaceHtmlByDict(value, dic)
    value = replaceDashAsNullString(value)

    car[key] = value







