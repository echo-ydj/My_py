# -*- coding:gbk -*-
""" print("hhhhhh\nasdadad")
n = 12
nn = 12
print("wm\n"*10)
print("{} is {}".format("a", "c"))
if 0 < n <= 12:
    print("000")
elif n < 10:
    print("sa")

"""

"""num = [1, 2, 3]
num.append("as")
for i in num:
    i = i+1
    i += 1
    print(i)"""
'''
i = 0
j = 0

while i < 4:

   # print("*", end="")
    while j < 5:
    #    j += 1

        print("*", end="")
        j = j + 1
    print()
    i += 1
'''
"""
for i in range(0, 10):
    for j in range(0, 6):
        print("*", end="")
    print()
    """
"""
num=int(input("shuruhang:"))
for i in range(1, num):
    for j in range(0, i):
        print("*", end="")
    print()
"""
"""
#num = int(input("shuru"))
i = 1
j = 1
for i in range(1, 9):
    for j in range(1, i):
        print("{} X {} = {}  ".format(j, i, i * j), end="")
    print()"""

"""
a = "asd"  \
    + "asd"
print(a)"""
"""
a = 120
b = chr(a)
c = str(a)
print("****%s" % type(b))
print(type(c))"""

"""
str1 = "asdfg123"
print(str1[2:5])             #dfg   前闭后开 取值个数5-2
print(str1[0:])              # asdfg123
print(str1[-1:0:-1])         # 321gfds
print(str1[-1::-1])          # 321gfdsa
print(str1[::-1])          # 321gfdsa
print(dir(str1))
"""

"""
def return_name():
    print("请输入一个名字:")
    name = input()
    return name


list = []
#name = ""
while True:
    print("======================")
    print("1.添加用户")
    print("2.删除用户")
    print("3.修改用户")
    print("4.查询用户")
    print("5.查看用户")
    print("q.退出程序")
    print("======================")
    str_num = input()
    if str_num == "Q" or str_num == "q":
        print("退出程序")
        break
    num = int(str_num)
    if num == 1:
        list.append(return_name())
    elif num == 2:
        list.remove(return_name())
    elif num == 3:
        name = return_name()
        print("请输入修改后用户名:")

        new_name = input()
        list[list.index(name)] = new_name

        pass
    elif num == 4:
        if return_name() in list:
            print("你所查找的用户在列表里中")
        else:
            print("你所查账的用户不在列表中")

    elif num == 5:
        if list :
            for list_name in list:
                print(list_name + "  ", end="")
                print()
        else:
            print("列表暂无数据")

    else:
        print("你输入有误程序退出")
"""
"""
list = []
while True:
    print("==================")
    print("1.添加名片")
    print("2.修改信息")
    print("3.删除名片")
    print("4.查询名片")
    print("==================")
    num = int(input())

    if num == 1:

        name = input("请输入姓名")
        phone = input("请输入电话")
        infor = {}
        infor["name"] = name
        infor["phone"] = phone
        list.append(infor)

    elif num == 2:
        name = input("请输入您要修改的姓名")
        for change_infor in list:
            if change_infor["name"] == name:
                print("name:{}   phone:{}".format(change_infor["name"], change_infor["phone"]))
                print("****************")
                print("1.修改用户名")
                print("2.修改电话")
                print("****************")
                num = int(input())
                if num == 1:
                    new_name = input("修改用户名为:")
                    change_infor["name"] = name
                elif num == 2:
                    new_name = input("修改电话为:")
                    change_infor["phone"] = phone

    elif num == 3:
        name = input("请输入要删除的姓名")
        for del_infor in list:
            if del_infor["name"] == name:
                n = list.index(del_infor)
                print("---------{}".format(n))
                list.remove(list[n])
    elif num == 4:
        name = input("请输入要查询的姓名")
        for show_infor in list:
            if show_infor["name"] == name:
                print("name:{}   phone:{}".format(show_infor["name"], show_infor["phone"]))
                break
            else:
                print("该用户不存在!")
                break
"""
"""
infor = {"name": "as"}
print(infor.get("name"))
"""
"global 全局局部变量"

# a = 12
#
#
# def a1():
#     """文档说明使用help(a1)时显示"""
#     # global a
#     a = 1       #修改全局变量需加 global
#     print(a)
# def a2():
#     print(a)   #全局变量 不能修改 否则会报错
# a2()
# a1()
# print(a)  #加 global a = 1 不加global a =12

# def two():
#     a = 1
#     b = 2
#     return a, b
#
#
# a, b = two()
# # a=5
# print(a)

# def sum_num(*args):
#     for num in args:
#         global Sum
#         Sum += num
#     return Sum
#
#
# Sum = 0
# print(sum_num(1, 2, 3))


"递归函数 自身函数体调用自身函数"
# def getnum(num):
#     if num > 1:
#         return num * getnum(num - 1)
#     else:
#         return num
#
#
# print(getnum(4))

"匿名函数"

# a = lambda x, y: x + y
#
# print(a(1, 2))

# def func(x):
#     return x > 3
#
#
# f_list = filter(func, [1, 2, 3, 4, 5])
# print([list for list in f_list])


# i = 0
# for i in range(0, 1):
#     print(id(i))
#
# print("waibu{}" .format( id(i)))


"文件操作-复制文件"
#
# file_read = open("C:\\Users\\asus\\Desktop\\Text.txt", "r")
#
# f = open("C:\\Users\\asus\\Desktop\\Text1.txt", "a")
# while True:
#     s = file_read.readline()
#
#     if s == "":   #判断是否读取到文件末尾
#         break
#     else:
#         f.write(s)
#
#
# f.flush()
# file_read.close()
# f.close()
# print("--")
"文件名修改"

# import os
#
# # print(os.getcwd()) 获取当前路径
# os.chdir("C:\\Users\\asus\Desktop\\12")  #修改当前路径
#
# list_name = os.listdir() #以列表形式传回文件名
# list_i = []
# for i in range(1, len(list_name) + 1):
#     list_i.append(str(i))
# print(list_i)
# num_n = 0
# for name in list_name:
#     print(num_n)
#     new_name = "Text" + list_i[num_n] + ".txt"
#     print(new_name)
#     os.rename(name, new_name)  #重命名
#     num_n += 1


# class people():
#     name = ""
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#      #   print(id(name))
#         return self.name  #必须为return self.name     return name报错
# a=people("123")
# n= a.get_name()
# print(n)

# class A:
#     num = 0  # 类属性
#     print(id(num))
#
#     # 实例方法
#     def __init__(self, name):
#         self.name = name
#         # 实例属性赋值（和对象有关的  有self都为实例属性）
#
#         A.num += 1  # 类属性加一
#         print(A.num)
#
#         # 类方法  格式@classmethod
#         # 类方法调用  类名.类方法 或 这个类创建的实例 实例.类方法
#     @classmethod
#     def add_num(cls):
#         cls.num += 1
#
#     # 静态方法   @staticmethod  可以不用self参数
#     # 方法调用    类名.静态方法  or  实例对象.静态方法
#     @staticmethod
#     def print():
#         print("0")
#
# A.add_num()
# A.print()
# m = A("123")
# n = A("1")


# class A(object):
#     str = None
#     flag = False
#
#     def __new__(cls, name):
#         if cls.flag == False:  # 或者 if cls.str == None
#             cls.str = object.__new__(cls)
#             cls.flag = True
#             return cls.str
#         else:
#             return cls.str
#
#     def __init__(self, name):
#
#         self.name = name
#         print(self.name)
#
#
# a = A("a")
# b = A("b")
# print(id(a))
# print(id(b))
# print(a.name)
# print(b.name)

"匿名函数"

# c=lambda x, y: x * y
# print(c(8,5))

# old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = list(map(lambda x: x * x, old_list))
# print(new_list)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# a = "[1,2,3]"
# c = [1,2]
# print(type(c))
# print(type(eval("[1,2,3]")))
# print(a[1])
# print(type(a))


# import Text2
# Text2.T2().t2()  #注意 T2（）   a = T2()
# a = Text2.T2()
# print(a.t2())


# class n(object):
#     __num = 10
#     nn = 10
#
#     def __init__(self):
#         pass
#
#     def setNum(self, new_num):
#         self.num = new_num
#         self.nn = 5
#
#     def getNum(self):
#         return self.num
#
#
# a = n()
# a.setNum(5)
# print(a.getNum())
# print(a.nn)


"导包"
# from TextMsg import nn
#
# nn.n()


"导入模块中的类"
"""
Text2.py

class T2(object):
    def t2(self):
        print("T2_t2")


n = T2()
n.t2()
"""

# import Text2
#
# a = Text2.T2()
# a.t2()


"闭包"

# def a1(n):
#     def a2(n1):
#         print("/////////")
#         print("A2")
#         print(n)
#         print(n1)
#
#     return a2(n)
#     return a2  # 返回a2的引用   <function __main__>
#


# a = a1(3)  # a = a2  a接收a2的引用
# a(5)  # a2()方法执行

# "装饰器"
# def A(func):
#     def aa():
#         print(aa)
#         func()         #执行传入函数
#         print(func)
#     return aa
# @A
# def b():
#     print(12)

# c = A(b)
#
# c()
# print(A(b))
# print(b)
# b


"两个装饰器时使用顺序"

#
#
# def a(func):
#     print("a")
#
#
# def b(func):
#     print("b")
#
#
# @a
# @b  # 从下到上先b  后 a
#
#
# def c():
#     print("c")


# c = lambda x:x*x
# print(c(2))
# a = [x for x in range(5)]
# print(a)

#
# def add(a, b, c):
#     re = a + b + c
#     return re
#
#
# def a_add(a, b):
#
#     re = 0
#     c = a + b + a
#     re = add(a, b, c) / 3
#     return re
#
#
# print(a_add(11, 12))


"""os.fork()  在windows 中 不能使用 只能在Linux中使用"""
# import  os
# a = os.fork()
# if a == 0:
#     for i in range(10):
#         print("///////")
# else:
#     for i in range(10):
#         print("*****")


# 注意import Process   Process(target=函数名)  大写P
# from multiprocessing import Process
# import time
# def test():
#     for i in range(4):
#         print("*", end="")
#         time.sleep(1)
#
# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start()
#     p.join()

# from multiprocessing import Process
#
# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


# 进程池
# from multiprocessing import Pool
# import time
# def test():
#     print("///")
#     time.sleep(2)
# #注意进程池使用应在main内 负责报错
# if __name__ == '__main__':
#     po = Pool(3)
#     po.apply_async(test)
#     po.close()
#     po.join()
#     print("00000")


# 有参传入
# import multiprocessing
# import time
# def func(msg):
#     print('msg: ', msg)
#     time.sleep(1)
#     print('----')
#
# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=4)
#     for i in range(10):
#         msg = 'hello world %d' % i
#         pool.apply_async(func, (msg, ))
#
#     pool.close()
#     pool.join()           #结束进程


# 进程间的通信  Process
# from multiprocessing import Queue
#
# q = Queue(3)        #
# q.put()           #写入
# q.get()           #获取
# q.full()          #是否满
# q.empty()         #是否存在

# 进程池间的通信
# from multiprocessing import Manager, Pool
# # if __name__ == '__main__':
# #     q = Manager().Queue()  # 使用Manger 中的Queue 初始化
# #     po = Pool()
# #     po.apply(函数,(参数,))
# #     po.close()
# #     po.join()


# 线程完成多任务
# from threading import Thread
# import time
#
#
# def test():
#     print("*********")
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     for i in range(0, 5):
#         t = Thread(target=test)
#         t.start()


# 进程间不共享任何数据   线程共享全局变量
# 线程间的全局变量间的传递
# from threading import Thread
# import time
# num = 10
# def add_num():
#     global num
#     num += 1
#     print("num:{}".format(num))
# def pr_num():
#     global num
#     num -= 1
#     print("num:{}".format(num))
# print("*-*-*-*-*-*-*-*")
# a = Thread(target=add_num)
# a.start()
# time.sleep(1)
# b = Thread(target=pr_num)
# b.start()


# 列表传递给线程
# from threading import Thread
# import time
#
# list_num = []
#
#
# def list_a(list_num):
#     list_num.append(10)
#
#
# def list_s(list_num):
#     print(list_num)
#
#
# t1 = Thread(target=list_a, args=(list_num,))
# t1.start()
#
# t2 = Thread(target=list_s, args=(list_num,))
# t2.start()


# 使用互斥锁
# 两个线程抢着上锁 如果一个线程上锁成功另一个线程只能等该线程锁解开后 执行上锁
from threading import Thread, Lock

# 创建一把互斥锁 默认没有锁上
lock_m = Lock()
num = 0


def add_num():
    global num
    lock_m.acquire()  # 上锁
    for i in range(100):
        num += 1
    lock_m.release()  # 解锁
    print("add_num---*---num:{}".format(num))


def add2_num():
    global num
    lock_m.acquire()
    for i in range(100):
        num += 1
    lock_m.release()
    print("add2_num---*---num:{}".format(num))


print("global---*---num:{}".format(num))
t1 = Thread(target=add_num)
t1.start()
t2 = Thread(target=add2_num)
t2.start()
