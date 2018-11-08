# -*- coding: utf-8 -*-

import re

text = '''
        var levelId =4;
        var keyLink = {"message":"<span class='hs_kw24_baikedG'></span>","result":{"total":218,"items":[{"name":"车型<span class='hs_kw88_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_19_567.html","id":567},{"name":"厂<span class='hs_kw68_baikedG'></span><span class='hs_kw55_baikedG'></span><span class='hs_kw106_baikedG'></span><span class='hs_kw52_baikedG'></span>(<span class='hs_kw65_baikedG'></span>)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_219.html","id":219},{"name":"厂<span class='hs_kw68_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_19_218.html","id":218},{"name":"级别","link":"http://car.autohome.com.cn/shuyu/detail_18_19_220.html","id":220},{"name":"发动机","link":"http://car.autohome.com.cn/shuyu/detail_8_9_555.html","id":555},{"name":"长*宽*高(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_222.html","id":222},{"name":"车身结构","link":"http://car.autohome.com.cn/shuyu/detail_3_4_281.html","id":281},{"name":"最高车速(km/h)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_267.html","id":267},{"name":"官方0-100km/h加速(s)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_225.html","id":225},{"name":"<span class='hs_kw79_baikedG'></span>0-100km/h加速(s)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_272.html","id":272},{"name":"<span class='hs_kw79_baikedG'></span>100-0km/h制动(m)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_273.html","id":273},{"name":"<span class='hs_kw79_baikedG'></span><span class='hs_kw19_baikedG'></span>(L/100km)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_243.html","id":243},{"name":"工信部<span class='hs_kw25_baikedG'></span><span class='hs_kw19_baikedG'></span>(L/100km)","link":"http://car.autohome.com.cn/shuyu/detail_18_19_271.html","id":271},{"name":"<span class='hs_kw79_baikedG'></span><span class='hs_kw3_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_306.html","id":306},{"name":"整车<span class='hs_kw91_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_19_274.html","id":274},{"name":"<span class='hs_kw59_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_275.html","id":275},{"name":"<span class='hs_kw23_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_276.html","id":276},{"name":"<span class='hs_kw45_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_277.html","id":277},{"name":"<span class='hs_kw53_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_3_4_132.html","id":132},{"name":"<span class='hs_kw14_baikedG'></span>轮距(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_278.html","id":278},{"name":"<span class='hs_kw104_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_638.html","id":638},{"name":"最小<span class='hs_kw3_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_279.html","id":279},{"name":"<span class='hs_kw6_baikedG'></span><span class='hs_kw95_baikedG'></span>(kg)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_280.html","id":280},{"name":"<span class='hs_kw11_baikedG'></span>(个)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_282.html","id":282},{"name":"座位数(个)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_283.html","id":283},{"name":"<span class='hs_kw4_baikedG'></span><span class='hs_kw76_baikedG'></span>(L)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_284.html","id":284},{"name":"行李厢<span class='hs_kw76_baikedG'></span>(L)","link":"http://car.autohome.com.cn/shuyu/detail_18_20_285.html","id":285},{"name":"发动机型<span class='hs_kw105_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_21_570.html","id":570},{"name":"<span class='hs_kw18_baikedG'></span>(mL)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_287.html","id":287},{"name":"<span class='hs_kw87_baikedG'></span>形式","link":"http://car.autohome.com.cn/shuyu/detail_18_21_640.html","id":640},{"name":"<span class='hs_kw92_baikedG'></span><span class='hs_kw39_baikedG'></span>形式","link":"http://car.autohome.com.cn/shuyu/detail_8_9_289.html","id":289},{"name":"<span class='hs_kw92_baikedG'></span>数(个)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_290.html","id":290},{"name":"每缸<span class='hs_kw10_baikedG'></span>(个)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_291.html","id":291},{"name":"压缩比","link":"http://car.autohome.com.cn/shuyu/detail_18_21_182.html","id":182},{"name":"<span class='hs_kw21_baikedG'></span><span class='hs_kw86_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_21_641.html","id":641},{"name":"<span class='hs_kw66_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_181.html","id":181},{"name":"<span class='hs_kw62_baikedG'></span>(mm)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_293.html","id":293},{"name":"<span class='hs_kw9_baikedG'></span>马力(Ps)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_294.html","id":294},{"name":"<span class='hs_kw9_baikedG'></span><span class='hs_kw37_baikedG'></span>(kW)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_295.html","id":295},{"name":"<span class='hs_kw9_baikedG'></span><span class='hs_kw37_baikedG'></span><span class='hs_kw7_baikedG'></span>(rpm)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_296.html","id":296},{"name":"<span class='hs_kw9_baikedG'></span><span class='hs_kw57_baikedG'></span>(N·m)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_571.html","id":571},{"name":"<span class='hs_kw9_baikedG'></span><span class='hs_kw57_baikedG'></span><span class='hs_kw7_baikedG'></span>(rpm)","link":"http://car.autohome.com.cn/shuyu/detail_18_21_642.html","id":642},{"name":"发动机特有技术","link":"http://car.autohome.com.cn/shuyu/detail_18_21_643.html","id":643},{"name":"燃料形式","link":"http://car.autohome.com.cn/shuyu/detail_18_21_572.html","id":572},{"name":"<span class='hs_kw75_baikedG'></span>标<span class='hs_kw105_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_21_573.html","id":573},{"name":"<span class='hs_kw20_baikedG'></span>方式","link":"http://car.autohome.com.cn/shuyu/detail_18_21_574.html","id":574},{"name":"<span class='hs_kw29_baikedG'></span>材料","link":"http://car.autohome.com.cn/shuyu/detail_18_21_575.html","id":575},{"name":"<span class='hs_kw58_baikedG'></span>材料","link":"http://car.autohome.com.cn/shuyu/detail_18_21_576.html","id":576},{"name":"<span class='hs_kw0_baikedG'></span><span class='hs_kw30_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_21_577.html","id":577},{"name":"简称","link":"http://car.autohome.com.cn/shuyu/detail_18_22_1072.html","id":1072},{"name":"挡位个数","link":"http://car.autohome.com.cn/shuyu/detail_18_22_559.html","id":559},{"name":"变速箱类型","link":"http://car.autohome.com.cn/shuyu/detail_18_22_221.html","id":221},{"name":"驱动方式","link":"http://car.autohome.com.cn/shuyu/detail_18_23_395.html","id":395},{"name":"四驱形式","link":"http://car.autohome.com.cn/shuyu/detail_3_7_412.html","id":412},{"name":"<span class='hs_kw34_baikedG'></span><span class='hs_kw102_baikedG'></span>结构","link":"http://car.autohome.com.cn/shuyu/detail_3_7_415.html","id":415},{"name":"<span class='hs_kw14_baikedG'></span><span class='hs_kw27_baikedG'></span>类型","link":"http://car.autohome.com.cn/shuyu/detail_18_23_578.html","id":578},{"name":"<span class='hs_kw17_baikedG'></span>类型","link":"http://car.autohome.com.cn/shuyu/detail_18_23_579.html","id":579},{"name":"<span class='hs_kw61_baikedG'></span>类型","link":"http://car.autohome.com.cn/shuyu/detail_18_23_510.html","id":510},{"name":"车体结构","link":"http://car.autohome.com.cn/shuyu/detail_3_4_223.html","id":223},{"name":"<span class='hs_kw14_baikedG'></span>制动器类型","link":"http://car.autohome.com.cn/shuyu/detail_18_24_511.html","id":511},{"name":"<span class='hs_kw100_baikedG'></span>类型","link":"http://car.autohome.com.cn/shuyu/detail_18_24_512.html","id":512},{"name":"<span class='hs_kw16_baikedG'></span>制动类型","link":"http://car.autohome.com.cn/shuyu/detail_18_24_513.html","id":513},{"name":"<span class='hs_kw14_baikedG'></span>轮胎<span class='hs_kw49_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_24_580.html","id":580},{"name":"<span class='hs_kw47_baikedG'></span><span class='hs_kw49_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_24_581.html","id":581},{"name":"<span class='hs_kw35_baikedG'></span><span class='hs_kw49_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_24_515.html","id":515},{"name":"主/副<span class='hs_kw93_baikedG'></span>座安全<span class='hs_kw63_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_45_1082.html","id":1082},{"name":"<span class='hs_kw14_baikedG'></span>/<span class='hs_kw71_baikedG'></span>侧<span class='hs_kw63_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=421","id":421},{"name":"<span class='hs_kw14_baikedG'></span>排侧<span class='hs_kw63_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=421","id":421},{"name":"<span class='hs_kw71_baikedG'></span>侧<span class='hs_kw63_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=421","id":421},{"name":"<span class='hs_kw14_baikedG'></span>/<span class='hs_kw71_baikedG'></span>头部<span class='hs_kw63_baikedG'></span>(气帘)","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=422","id":422},{"name":"<span class='hs_kw14_baikedG'></span>排头部<span class='hs_kw63_baikedG'></span>(气帘)","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=422","id":422},{"name":"<span class='hs_kw71_baikedG'></span>头部<span class='hs_kw63_baikedG'></span>(气帘)","link":"http://car.autohome.com.cn/shuyu/detail_18_45_420.html?lang=422","id":422},{"name":"膝部<span class='hs_kw63_baikedG'></span>","link":"http://car.autohome.com.cn/shuyu/detail_16_17_420.htm…'''

data = re.search('var levelId =.*', text, re.DOTALL).group()
if data:
        print(data)
else:
        print('None')