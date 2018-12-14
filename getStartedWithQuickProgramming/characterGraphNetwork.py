# -*- coding: utf-8 -*-
# 假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样：
# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]
# 你可以认为grid[x][y]是一幅“图”在x、y 坐标处的字符，该图由文本字符组成。
# 原点(0, 0)在左上角，向右x 坐标增加，向下y 坐标增加。
# 复制前面的网格值，编写代码用它打印出图像。
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

i = 0
j = 0
while i < 9:
    while j < 6:
        print(grid[i][j], end='')
        i += 1
        if i == 9:
            print('\n')
            i = 0
            j += 1




