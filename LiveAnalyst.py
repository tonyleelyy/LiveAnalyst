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

# 目的地弹幕判断词
tar_str = '目的地 '

# 管理员命令弹幕判断词
admin_str = 'TonyLee_Lyy 說: 清除行 '

# 检测延迟
delay = 1

# 读取判断词长度（含空格）
tar_len = len(tar_str)
admin_len = len(admin_str)

history = '1'

# 读取最后一行弹幕
def readline():
    with open(fp.txtpath, 'r', encoding='utf-8') as tf:
        lines = tf.readlines()
        global last_line
        last_line = lines[-1]
    tf.close()

# 判断是否含有'目的地'字符串
def check_location():
    global check_location_result
    check_location_result = tar_str in last_line

# 读取弹幕中的目的地
def readlocation():
    global index
    index = last_line.find('%s' %(tar_str)) + tar_len
    global location
    location = last_line[index:]

# 执行添加目的地操作
def add():
    with open(fp.respath,"r",encoding='utf-8') as rf:
        alllines = rf.readlines()
    if location in alllines:
        print('检测到目的地：%s，但目的地已存在！' %(location))
    else:
        print('检测到目的地：%s' %(location))
        with open(fp.respath,"a",encoding='utf-8') as rw:
            rw.write("%s" %(last_line[index:]))
        rw.close()
    rf.close()

# 判断是否含有管理员命令
def check_admin():
    global check_admin_result
    check_admin_result = admin_str in last_line

# 执行管理员命令
def admin_action():
    if check_admin_result == True:
        print('\n检测到管理员命令！')
        location_count = last_line[index:]
        location_count_index = last_line.find('%s' %(admin_str)) + admin_len
        tar_line = last_line[location_count_index:]
        tar_line_int = int(tar_line)
        with open(fp.respath, 'r', encoding='utf-8') as old_file:
            with open(fp.respath, 'r+', encoding='utf-8') as new_file:
                current_line = 0
                while current_line < (tar_line_int - 1):
                    old_file.readline()
                    current_line += 1
                
                seek_point = old_file.tell()
                new_file.seek(seek_point, 0)
                old_file.readline()
                next_line = old_file.readline()
                while next_line:
                    new_file.write(next_line)
                    next_line = old_file.readline()
                
                new_file.truncate()
            new_file.close()
        old_file.close()
    else:
        print('\n没有检测到管理员命令。')

# 读取文本内的行数
def count():
    with open(fp.respath,'a+',encoding='utf-8') as tf:
        global countline
        countline = len(tf.readlines())
    tf.close()

# 主程序
while True:
    # 函数初始化
    check_location_result = False
    check_admin_result = False
    last_line = '1'
    countline = 0
    location = 'China'
    index = 0
    
    # 循环步骤
    readline() # 读取最后一行弹幕
    if history == last_line:
        print('\n没有新弹幕。')
    else:
        history = last_line
        check_admin() # 判断是否含有管理员命令
        admin_action() # 执行管理员命令
        check_location() # 判断是否含有'目的地'字符串
        if check_location_result == True:
            readlocation() # 读取弹幕中的目的地
            add() # 执行添加目的地操作
        else:
            print('没有检测到目的地。')
            location = '1'
    time.sleep(delay)