# coding=utf8
__author__ = 'ives'

import FileOut
import sys
import os
import GetThread


start = 266627
end = 358797

# 重定向print输出到文件
file_out = FileOut.FileOut(sys.stdout)
sys.stdout = file_out

# 生成数字的列表
i = start
num = []
while i <= end:
    if not os.path.exists("./art/%d.txt" % i):
        print "[INFO]Exist: %d" % (i, )
        num.append(i)

    i += 2

# 10条线程
n = len(num)
m = int(n/8)
threads = []
for i in range(8):
    th = GetThread.GetThread(i, start+i*m, start+(i+1)*m-1)
    th.start()
    threads.append(th)

for t in threads:
    t.join()








