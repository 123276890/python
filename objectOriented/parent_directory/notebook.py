# -*- coding: utf-8 -*-

import datetime

# 为所有新的备注存储下一个可用的id
last_id = 0


class Note:
    """代表笔记本上的一个笔记。在每个注释的搜索和存储标记中匹配字符串"""

    def __init__(self, memo, tages=''):
        """使用备忘录和可选的空格分隔标记初始化注释。自动设置笔记的创建日期和唯一id"""
        self.memo = memo
        self.tags = tages
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """确定此注释是否对筛选器测试进行数学运算。如果匹配返回true，否则返回false
            搜索是区分大小写的，并且匹配文本和标记"""

        return filter in self.memo or filter in self.tags


class Notebook:
    """表示可以标记、修改和搜索的注释集合"""

    def __init__(self):
        """用空列表初始化一个笔记本"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """创建一个新注释并将其添加到列表中"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """找到具有给定id的注释"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_memo(self, note_id, memo):
        """找到具有给定id的注释，并将其标记更改为给定值"""
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = memo
        #         break
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """找到具有给定id的注释，并将其标记更改为给定值"""
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.tags = tags
        #         break
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        """查找与给定过滤器字符串匹配的所有注释"""
        return [note for note in self.notes if note.match(filter)]