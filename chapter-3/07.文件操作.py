#读文件

"""
路径写法:
        相对路径:从当前文件所在目录开始查找
        . :表示当前路径
        ..:表示上一级目录
绝对路径:
        从文件系统根目录开始查找，需要文件位置的完整路径(注意:\\转义或者/)
"""

# with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
#     f.write("静夜思(李白)\n\n")
#     f.write("窗前明月光,\n")
#     f.write("疑是地上霜,\n")
#     f.write("举头望明月,\n")
#     f.write("低头思故乡,\n")


with open("./resources/静夜思.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)


#写文件
#a: append, 追加内容;w: 覆盖内容;文件不存在则创建文件
with open("./resources/静夜思.txt","a",encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光,\n")
    f.write("疑是地上霜,\n")
    f.write("举头望明月,\n")
    f.write("低头思故乡,\n")
