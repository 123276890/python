# -*- coding: utf-8 -*-

"""
假设你有一项无聊的工作，要调整数千张图片的大小，并在每张图片的角上增
加一个小徽标水印。使用基本的图形程序，如Paintbrush 或Paint，完成这项工作需
要很长时间。像Photoshop 这样神奇的应用程序可以批量处理，但这个软件要花几
百美元。
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
            or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        im.save(os.path.join('withLogo', filename))