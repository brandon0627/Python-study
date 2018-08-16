# coding: utf-8
# if True:
#     print "True"
# else:
#     print "False"
#
# if True:
#   print "Answer"
#   print "True"
# else:
#   print "Answer"
#   print "False"

# 这是注释
# a = 1
# b = "a"
# print a,b

# total = item_one + \
#         item_two + \
#         item_three

# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']

# print days[1]

# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。
# 包含了多个语句"""

# raw_input("按下 enter 键退出，其他任意键显示...\n")  # 按键才走下一步

# print paragraph

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# s = "123456"
# print s[1:5] *2

# 列表List
# list = ['runoob', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']
#
# print "完整列表=",list  # 输出完整列表
# list[1] = 1000
# print "完整列表=",list  # 输出完整列表
# print list[0]  # 输出列表的第一个元素
# print list[1:3]  # 输出第二个至第三个元素
# print list[2:]  # 输出从第三个开始至列表末尾的所有元素
# print tinylist * 2  # 输出列表两次
# print list + tinylist  # 打印组合的列表

# 元素组type
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print tuple  # 输出完整元组
# print tuple[0]  # 输出元组的第一个元素
# print tuple[1:3]  # 输出第二个至第三个的元素
# print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2  # 输出元组两次
# print tuple + tinytuple  # 打印组合的元组
#
# tuple[1] = 1000 # 错误，不允许再次赋值
# print tuple  # 输出完整元组

# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# print dict['one']  # 输出键为'one' 的值
# print dict[2]  # 输出键为 2 的值
# print tinydict  # 输出完整的字典
# print tinydict.keys()  # 输出所有键
# print tinydict.values()  # 输出所有值
#
# print dict.keys()  # 输出所有键
# print dict.values()  # 输出所有值

# 类型转换
# tinytuple = (123, 'john')
# list = list(tinytuple)
# list[0] = 100
#
# print list

# str ="{'a':'张三','b':'李四'}"

# dict = dict(a='a', b='b', t='t')
# print dict['a']

def print_func( par ):
   print "Hello : ", par
   return