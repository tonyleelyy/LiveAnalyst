import os
import time
import datetime

# 文件保存地址
class FilePath:
    folder = "D:\OneDrive\OneDrive - ofistbsteduau.onmicrosoft.com\文档\弹幕姬" # 存储弹幕文本的文件夹，默认为文档目录
    curr_time = datetime.datetime.now()
    txtfront = curr_time.strftime("%Y-%m-%d")
    txtname = "%s.txt" %(txtfront)
    txtpath = "%s/%s" %(folder, txtname)
    respath = "%s/result.txt" %(folder)
fp = FilePath()

# 读取txt最后一行
def readline():
    with open(fp.txtpath, 'r', encoding='utf-8') as tf:
        lines = tf.readlines()
        global last_line
        last_line = lines[-1]
    tf.close()

def check():
    tar_str = '目的地'
    global result
    result = tar_str in last_line

while True:
    result = False
    last_line = '1'
    count = len(open(fp.respath,'a+',encoding='utf-8').readlines())
    if count >= 5:
        print('列表已满！')
        time.sleep(600)
    else:
        readline()
        check()
        if result == True:
            index = last_line.find('目的地')+4
            location = last_line[index:]

            with open(fp.respath,"r",encoding='utf-8') as rf:
                alllines = rf.readlines()
                if location in alllines:
                    print('目的地已存在！')
                else:
                    print('检测到目的地：%s' %(location))
                    with open(fp.respath,"a",encoding='utf-8') as rw:
                        rw.write("%s" %(last_line[index:]))
            rf.close()
            time.sleep(1)
        else:
            print('目的地没检测到！')
            location = '2'
            time.sleep(1)