# -*- coding: utf-8 -*-
"""
创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本
文件中出现ADJECTIVE、NOUN、ADVERB 或VERB 等单词的地方，加上他们自
己的文本。
"""

import re

madlist = open('/Users/zhuangganglong/python/getStartedWithQuickProgramming/madList.txt')
madlistContent = madlist.read()
madlistContent = madlistContent.split()
for i, v in enumerate(madlistContent):
    if v.count('ADJECTIVE') > 0:
        print('Enter an adjective:')
        adjective = input()
        madlistContent[i] = adjective
    elif v.count('NOUN') > 0:
        print('Enter an noun:')
        noun = input()
        madlistContent[i] = noun
    elif v.count('ADVERB') > 0:
        print('Enter an adverb:')
        adverb = input()
        madlistContent[i] = adverb
    elif v.count('VERB') > 0:
        print('Enter an verb:')
        if v == 'VERB':
            verb = input()
            madlistContent[i] = verb
        else:
            v = re.compile(r'(VERB)(\S*)').search(v).group(2)
            verb = input()
            madlistContent[i] = verb + v
madlistContent = ' '.join(madlistContent)
print(madlistContent)
newMadList = open('/Users/zhuangganglong/python/getStartedWithQuickProgramming/newMadList.txt', 'w')
newMadList.write(madlistContent)
newMadList.close()