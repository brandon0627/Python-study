# *_*coding:utf-8 *_*
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : ", self.name, ", Salary: ", self.salary

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : ", self.name, ", Salary: ", self.salary
#
#
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# # emp1.displayEmployee()
# # emp2.displayEmployee()
# # print "Total Employee %d" % Employee.empCount
# # print emp1.empCount
#
# hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
# getattr(emp1, 'empCount')    # 返回 'age' 属性的值
# setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
# delattr(emp1, 'age')    # 删除属性 'age'
# emp1.displayEmployee()

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print self.__secretCount
#
#     def getSecretCount(self):
#         return self.__secretCount
#
# counter = JustCounter()
# counter.count()
# print counter.getSecretCount()
# print counter.publicCount
# # print counter.__secretCount  # 报错，实例不能访问私有变量

# from file import a
#
# a()

# class Runoob:
#     __site = "www.runoob.com"
#
# runoob = Runoob()
# print runoob._Runoob__site

# import re
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

# import re
#
# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
#     print "searchObj.group(1) : ", searchObj.group(1)
#     print "searchObj.group(2) : ", searchObj.group(2)
# else:
#     print "Nothing found!!"

import re

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"