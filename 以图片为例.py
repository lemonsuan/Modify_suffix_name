import os

# 列表接收当前文件夹中文件名
files = os.listdir('.')
# 遍历每一个
for fileName in files:
    # 元组接收分离开的文件名以及后缀名
    portion = os.path.splitext(fileName)
    # 如果后缀是.png
    if portion[1] == ".png":
        # 重新组合文件名和后缀名
        newName = portion[0] + ".jpg"
        os.rename(fileName, newName)

