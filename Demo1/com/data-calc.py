# *_*coding:utf-8 *_*
# a,b = 2,5.0
# # print a+b
# b = a+b
# # print a+b
# print b/a
# print b//a
# print b%a
# print b**a

# a = 20
# b = 20
# if (a is b):
#     print "1 - a 和 b 有相同的标识"
# else:
#     print "1 - a 和 b 没有相同的标识"
#
# if (a is not b):
#     print "2 - a 和 b 没有相同的标识"
# else:
#     print "2 - a 和 b 有相同的标识"

# count = 0
# while (count < 9):
#     print 'The count is:', count
#     count +=  1
# print "Good bye!"

# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:  # 非双数时跳过输出
#         continue
#     print i  # 输出双数2、4、6、8、10
#
# i = 1
# while 1:  # 循环条件为1必定成立
#     print i  # 输出1~10
#     i += 1
#     if i > 10:  # 当i大于10时跳出循环
#         break

# var = 1
# while var == 1:  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print "You entered: ", num
#
# print "Good bye!"

# str = "dsadsafsa";
# print str.split("a");
# print str.split(' ', 1 );
#
# print str.upper()
#
# print max(str)


# str = "-";
# seq = ("a", "b", "c"); # 字符串序列
# print str.join( seq );
#
# str.lstrip()

# list1, list2 = [123, 'xyz'], [456, 'abc']
#
# print cmp(list1, list2);
# print cmp(list2, list1);
# list3 = list2 + [786];
# print cmp(list2, list3)

# aList = [123, 'xyz', 'zara', 'abc'];
#
# print "Index for xyz : ", aList.index( 'xyz' ) ;
# print "Index for zara : ", aList.index( 'zara' ) ;

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
#
# print "dict['Alice']: ", dict.get('Alice','没有值')


# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
# print "字典值 : %s" % dict.items()
#
# # 遍历字典列表
# for key, values in dict.items():
#     print key, values

# print 239%7

# site= {'name': "菜鸟教程", 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.popitem()
# print(pop_obj)
# print(site)
#
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.pop('name')
# print pop_obj    # 输出 ：菜鸟教程
# print site

# import time
#
# print "Start : %s" % time.ctime()
# time.sleep(5)
# print "End : %s" % time.ctime()
