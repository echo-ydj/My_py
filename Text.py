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
print(str1[2:5])             #dfg   ǰ�պ� ȡֵ����5-2
print(str1[0:])              # asdfg123
print(str1[-1:0:-1])         # 321gfds
print(str1[-1::-1])          # 321gfdsa
print(str1[::-1])          # 321gfdsa
print(dir(str1))
"""

"""
def return_name():
    print("������һ������:")
    name = input()
    return name


list = []
#name = ""
while True:
    print("======================")
    print("1.����û�")
    print("2.ɾ���û�")
    print("3.�޸��û�")
    print("4.��ѯ�û�")
    print("5.�鿴�û�")
    print("q.�˳�����")
    print("======================")
    str_num = input()
    if str_num == "Q" or str_num == "q":
        print("�˳�����")
        break
    num = int(str_num)
    if num == 1:
        list.append(return_name())
    elif num == 2:
        list.remove(return_name())
    elif num == 3:
        name = return_name()
        print("�������޸ĺ��û���:")

        new_name = input()
        list[list.index(name)] = new_name

        pass
    elif num == 4:
        if return_name() in list:
            print("�������ҵ��û����б�����")
        else:
            print("�������˵��û������б���")

    elif num == 5:
        if list :
            for list_name in list:
                print(list_name + "  ", end="")
                print()
        else:
            print("�б���������")

    else:
        print("��������������˳�")
"""
"""
list = []
while True:
    print("==================")
    print("1.�����Ƭ")
    print("2.�޸���Ϣ")
    print("3.ɾ����Ƭ")
    print("4.��ѯ��Ƭ")
    print("==================")
    num = int(input())

    if num == 1:

        name = input("����������")
        phone = input("������绰")
        infor = {}
        infor["name"] = name
        infor["phone"] = phone
        list.append(infor)

    elif num == 2:
        name = input("��������Ҫ�޸ĵ�����")
        for change_infor in list:
            if change_infor["name"] == name:
                print("name:{}   phone:{}".format(change_infor["name"], change_infor["phone"]))
                print("****************")
                print("1.�޸��û���")
                print("2.�޸ĵ绰")
                print("****************")
                num = int(input())
                if num == 1:
                    new_name = input("�޸��û���Ϊ:")
                    change_infor["name"] = name
                elif num == 2:
                    new_name = input("�޸ĵ绰Ϊ:")
                    change_infor["phone"] = phone

    elif num == 3:
        name = input("������Ҫɾ��������")
        for del_infor in list:
            if del_infor["name"] == name:
                n = list.index(del_infor)
                print("---------{}".format(n))
                list.remove(list[n])
    elif num == 4:
        name = input("������Ҫ��ѯ������")
        for show_infor in list:
            if show_infor["name"] == name:
                print("name:{}   phone:{}".format(show_infor["name"], show_infor["phone"]))
                break
            else:
                print("���û�������!")
                break
"""
"""
infor = {"name": "as"}
print(infor.get("name"))
"""
"global ȫ�־ֲ�����"

# a = 12
#
#
# def a1():
#     """�ĵ�˵��ʹ��help(a1)ʱ��ʾ"""
#     # global a
#     a = 1       #�޸�ȫ�ֱ������ global
#     print(a)
# def a2():
#     print(a)   #ȫ�ֱ��� �����޸� ����ᱨ��
# a2()
# a1()
# print(a)  #�� global a = 1 ����global a =12

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


"�ݹ麯�� �����������������"
# def getnum(num):
#     if num > 1:
#         return num * getnum(num - 1)
#     else:
#         return num
#
#
# print(getnum(4))

"��������"

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


"�ļ�����-�����ļ�"
#
# file_read = open("C:\\Users\\asus\\Desktop\\Text.txt", "r")
#
# f = open("C:\\Users\\asus\\Desktop\\Text1.txt", "a")
# while True:
#     s = file_read.readline()
#
#     if s == "":   #�ж��Ƿ��ȡ���ļ�ĩβ
#         break
#     else:
#         f.write(s)
#
#
# f.flush()
# file_read.close()
# f.close()
# print("--")
"�ļ����޸�"

# import os
#
# # print(os.getcwd()) ��ȡ��ǰ·��
# os.chdir("C:\\Users\\asus\Desktop\\12")  #�޸ĵ�ǰ·��
#
# list_name = os.listdir() #���б���ʽ�����ļ���
# list_i = []
# for i in range(1, len(list_name) + 1):
#     list_i.append(str(i))
# print(list_i)
# num_n = 0
# for name in list_name:
#     print(num_n)
#     new_name = "Text" + list_i[num_n] + ".txt"
#     print(new_name)
#     os.rename(name, new_name)  #������
#     num_n += 1


# class people():
#     name = ""
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#      #   print(id(name))
#         return self.name  #����Ϊreturn self.name     return name����
# a=people("123")
# n= a.get_name()
# print(n)

# class A:
#     num = 0  # ������
#     print(id(num))
#
#     # ʵ������
#     def __init__(self, name):
#         self.name = name
#         # ʵ�����Ը�ֵ���Ͷ����йص�  ��self��Ϊʵ�����ԣ�
#
#         A.num += 1  # �����Լ�һ
#         print(A.num)
#
#         # �෽��  ��ʽ@classmethod
#         # �෽������  ����.�෽�� �� ����ഴ����ʵ�� ʵ��.�෽��
#     @classmethod
#     def add_num(cls):
#         cls.num += 1
#
#     # ��̬����   @staticmethod  ���Բ���self����
#     # ��������    ����.��̬����  or  ʵ������.��̬����
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
#         if cls.flag == False:  # ���� if cls.str == None
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

"��������"

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
# Text2.T2().t2()  #ע�� T2����   a = T2()
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


"����"
# from TextMsg import nn
#
# nn.n()


"����ģ���е���"
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


"�հ�"

# def a1(n):
#     def a2(n1):
#         print("/////////")
#         print("A2")
#         print(n)
#         print(n1)
#
#     return a2(n)
#     return a2  # ����a2������   <function __main__>
#


# a = a1(3)  # a = a2  a����a2������
# a(5)  # a2()����ִ��

# "װ����"
# def A(func):
#     def aa():
#         print(aa)
#         func()         #ִ�д��뺯��
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


"����װ����ʱʹ��˳��"

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
# @b  # ���µ�����b  �� a
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


"""os.fork()  ��windows �� ����ʹ�� ֻ����Linux��ʹ��"""
# import  os
# a = os.fork()
# if a == 0:
#     for i in range(10):
#         print("///////")
# else:
#     for i in range(10):
#         print("*****")


# ע��import Process   Process(target=������)  ��дP
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


# ���̳�
# from multiprocessing import Pool
# import time
# def test():
#     print("///")
#     time.sleep(2)
# #ע����̳�ʹ��Ӧ��main�� ���𱨴�
# if __name__ == '__main__':
#     po = Pool(3)
#     po.apply_async(test)
#     po.close()
#     po.join()
#     print("00000")


# �вδ���
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
#     pool.join()           #��������


# ���̼��ͨ��  Process
# from multiprocessing import Queue
#
# q = Queue(3)        #
# q.put()           #д��
# q.get()           #��ȡ
# q.full()          #�Ƿ���
# q.empty()         #�Ƿ����

# ���̳ؼ��ͨ��
# from multiprocessing import Manager, Pool
# # if __name__ == '__main__':
# #     q = Manager().Queue()  # ʹ��Manger �е�Queue ��ʼ��
# #     po = Pool()
# #     po.apply(����,(����,))
# #     po.close()
# #     po.join()


# �߳���ɶ�����
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


# ���̼䲻�����κ�����   �̹߳���ȫ�ֱ���
# �̼߳��ȫ�ֱ�����Ĵ���
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


# �б��ݸ��߳�
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


# ʹ�û�����
# �����߳��������� ���һ���߳������ɹ���һ���߳�ֻ�ܵȸ��߳����⿪�� ִ������
from threading import Thread, Lock

# ����һ�ѻ����� Ĭ��û������
lock_m = Lock()
num = 0


def add_num():
    global num
    lock_m.acquire()  # ����
    for i in range(100):
        num += 1
    lock_m.release()  # ����
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
