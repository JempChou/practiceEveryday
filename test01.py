'''
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 

环境：windows10 64 ，pycharm2017.1.1 ,python3
editor:jempchou
'''

from PIL import Image, ImageFont, ImageDraw  # 从PIL库导入所需模块
import sys

# 头像图片路径
inputFile = r"resources/input.jpg"
# 处理后输出路径
outputFile = r"resources/output.jpg"
# 字体路径
fontPath = r"resources/Coval.otf"

# 打开图片，建立画布
image = Image.open(inputFile, 'r')
draw = ImageDraw.Draw(image)

# 由图片大小确定字体大小
fontsize = min(image.size) / 4

# 增加文字
fontobj = ImageFont.truetype(font=fontPath, size=round(fontsize), index=0, encoding='')  # 实例字体对象
draw.text((image.size[0] - fontsize, 0), text="4", fill=(255, 0, 0), font=fontobj,
          anchor=None)  # 用draw对象的text()方法添加文字
image.save(outputFile)  # 保存图片
