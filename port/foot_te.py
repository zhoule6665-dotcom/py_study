def my_open():
    f = open("/home/dr/py/port/foot.txt","r+")
    while 1:
        get = input("输入文字<==>-1退出")
        if get == "-1":
            f.close()
            break
        f.write(get)
    else:
        print("退出")
if "__name__"=="__main__":
    my_open()
