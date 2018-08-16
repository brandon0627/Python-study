# *_*coding:utf-8 *_*

# 打开一个文件
# fo = open("foo.txt", "r+")
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace

# fo.write( "www.runoob.com!\nVery good site!\n")
# fo.write("这里是一个文件")

# fo = open("foo.txt", "r+")
# str = fo.read(10)
# print "读取的字符串是 : ", str
#
# # 关闭打开的文件
# fo.close()

# import os

# 重命名文件test1.txt到test2.txt。
# os.rename("foo.txt", "test1.txt")

# os.remove("test1.txt")

# import os
# os.mkdir("newdir")
# os.remove("newdir")

# import sys,time
# for i in range(10): #进度条类型
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.2)

# 打开文件
# fo = open("runoob.txt", "wb")
# print "文件名为: ", fo.name
#
# # 刷新缓冲区
# fo.flush()
#
# # 关闭文件
# fo.close()

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"
# else:
#     print "内容写入文件成功"
#     fh.close()

# import os
# os.removedirs("newdir")
# try:
#     a = 4 / 1
# except :
#     print "错误"
# else:
#     print "正常"

import os, sys

# 假定 /tmp/foo.txt 文件存在，并有读写权限

# fh = open("testfile", "w")
# fh.close()
# os.rename("testfile","foo.txt")
# ret = os.access("foo.txt", os.F_OK)
# print "F_OK - 返回值 %s"% ret
#
# ret = os.access("foo.txt", os.R_OK)
# print "R_OK - 返回值 %s"% ret
#
# ret = os.access("foo.txt", os.W_OK)
# print "W_OK - 返回值 %s"% ret
#
# ret = os.access("foo.txt", os.X_OK)
# print "X_OK - 返回值 %s"% ret

def a():
    print "a"