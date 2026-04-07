import time
def timeTL():
    ticks = time.time()
    print(f"时间戳为{ticks}")
    localtime = time.localtime(time.time())
    print(f"本地时间为 :{localtime}")
    return 0


