# -*- coding: UTF-8 -*-

# file = open("gamePlay.mp3", 'rb')
file = open("贝瓦儿歌-小星星.mp3", 'rb')
# file = open("Charlie Puth-The Moment.mp3", 'rb')
# file = open("Thomas Greenberg - Easy Breeze.mp3", 'rb')
# file = open("原来.mp3", 'rb')
data = file.read()
file.close()

# 找到header位置


def TIT2():
    # 获取内容
    print(type(data))
    # 找到header位置，后4字节转10进制
    # 判断是否找到
    posstion = data.find("TIT2".encode())
    print(posstion)
    print("possion类型：", type(posstion))
    print("data类型：", type(data))
    # count = data[posstion + 4:posstion + 8]
    # sums = (count[0]) * 0x100000000 + count[1] * 0x10000 + count[2] * 0x100 + count[3]
    # content = data[posstion + 10:posstion + 10 + sums]
    # songname = content.decode("UTF-8", "ignore")
    # print(content[0], content[1], content[2], content[3], content[4], content[5], content[6])
    # print(sums)
    # print(content)
    # print(songname)

    if "TIT2" in data.decode("UTF-8", "ignore"):
        count = data[posstion + 4:posstion + 8]
        print(count.decode("UTF-8", "ignore"))
        sums = (count[0]) * 0x100000000 + count[1] * 0x10000 + count[2] * 0x100 + count[3]
        print("sums类型：", type(sums))
        content = data[(posstion + 10):(posstion + 10 + sums)]
        songname = content.decode("UTF-8", "ignore")
        print("possion类型：", type(posstion))
        
        print(songname)
    else:
        return


TIT2()
