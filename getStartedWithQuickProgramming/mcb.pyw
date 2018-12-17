# -*- coding: utf-8 -*-

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#   py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
"""
假定你有一个无聊的任务，要填充一个网页或软件中的许多表格，其中包含一
些文本字段。剪贴板让你不必一次又一次输入同样的文本，但剪贴板上一次只有一
个内容。如果你有几段不同的文本需要拷贝粘贴，就不得不一次又一次的标记和拷
贝几个同样的内容。
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# 保存剪贴板内容。
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # 列出关键字和加载内容。
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
mcbShelf.close()
