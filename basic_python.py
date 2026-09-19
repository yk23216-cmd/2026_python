# \n是換行符號
# print("第一行\n第二行")

# 變數
# (變數的第一個字不能是數字)
# (變數不能是保留字)
# (變數可以是數字、字母、底線)
# (變數有int float str bool等型態)

# int  整數
# x = 10
# y = -5
# print(x)

# float  浮點數
# pi = 3.14
# g = 5.0
# print(pi)

# str  字串(可使用單引號或雙引號)
# n = "5"
# name = "Sandy"
# color = "紫色"
# print(name)

# bool  布林值(T和F需要大寫)
# a = True
# b = False

# 字串相加就是相連
# print("字串相加" + "就是相連")
# 字串乘以數字就是重複
# print( "hello" * 5)
# 整數不可和字串相加

# type()可以查詢變數的型態
# a = "10"
# print(type(a))

# 轉換型別
# a = "5"
# b = float(a)
# print(b)

# print預設是換行
# hello python
# print("hello", end=" ")  # end = "想要的區隔方式"
# print("python")
# print("apple", end=":")
# print(15)

# 字串區隔
# print("apple" + "banana" + "mango") # applebananamango
# print("apple", "banana", "mango") # apple banana mango

# 字串切片
# a = "wejrijer133o"
# print(a[1:4]) # ejr

# 字串格式化
# 1.要印的寫在""裡
# 2.變數用%來代替
# 3.引號後面接%(變數)
# a = "apple"
# b = "mango"
# c = "banana"
# d = 70
# print("%s和%s最近很便宜，%s最近一個賣%s元" % (a, c, b, d))

# 字串格式化(f-string)

# name = "sandy"
# age = 15
# print(f"{name}現在{age}歲")  # sandy現在15歲

# 算術運算子

#  +是相加
# print(x+y)
#  -是相減
# print(x-y)
#  *是相乘
# print(x*y)
#  /是相除
# print(x/y)
#  //是整數除法(取商數)
# print(x//y)
#  %是取餘數
# print(x%y)
#  **是次方
# print(x**y)

# height = 1.7
# weight = 60
# height = height**2
# BMI = weight/height
# print(BMI)

# x = 5
# x += 10#等同於x=x+10
# print(x)

# 比較運算子
# == 判斷兩者是否相等
# != 判斷兩者是否不同
# >  大於
# <  小於
# >= 大於等於
# <= 小於等於

# print(5 == "5")  # False
# print(5 == 5)  # True
# print(5 != 5)  # False
# print(5 >= 5)  # True
# x = 5
# print(1 < x <= 6)  # True

# 邏輯運算子
# and #兩個條件都成立才是True
# print(True and True)#True
# print(True and False)#False
# or #只要一個條件成立就是True
# print(True or False)#True
# print(5>3 or 5>6)#True
# not #相反
# print(not True)#False
# 邏輯運算子優先順序 not>and>or
# print(not (True or False) and False)  # False

# list 列表(命名規則和變數一樣)
# 列表 = [ , ]
# a = [10,20,30]#建立列表
# b = []#建立空列表
# c = [10, "hello", "1000", True]  # python列表內可以放不同資料型態

# fruits = ["apple", "banana", "orange"]
# 印出單一值
# print(fruits[1]) # banana
# 印出整個列表
# print(fruits) # ["apple", "banana", "orange"]
# 印出多個值
# 列表[索引:索引+1]
# print(fruits[1:3]) # ["banana", "orange"]

# 列表新增元素
# 列表名稱.append(新增的元素)
# shopping = ["milk", "egg"]
# shopping.append("rice")
# print(shopping)# append()將元素新增至列表最後面
# 列表名稱.insert(插入的索引, 新增的元素)
# a = [3, 7, 2, 5]
# a.insert(2, 6)  # insert()將元素插入到指定位置
# print(a)

# 列表刪除元素
# del 列表名稱[索引]
# number = [2, 4, 6, 8]
# del number[1]  # del 指定索引將該元素刪除
# print(number)  # [2, 6, 8]
# 列表名稱.remove(元素)
# number = [2, 4, 6, 8]
# number.remove(4)  # remove是指定元素刪除
# print(number)  # [2, 6, 8]

# 指定列表排序
# 由小到大排序
# 列表名稱 = ["c", "a", "d", "b"]
# 列表名稱.sort()  # sort將列表由小到大排序
# print(列表名稱)  # ["a", "b", "c", "d"]
# 由大到小排序
# 列表名稱 = [20, 10, 50, 30]
# 列表名稱.sort(reverse = True)  # sort(reverse = True)將列表由大到小排序
# print(列表名稱)  # [50, 30, 20, 10]
# 反轉列表
# 列表名稱.reverse()
# name = ["小名", "小成", "小品", "小韋"]
# name.reverse()  # reverse 反轉列表
# print(name)  # ["小韋", "小品", "小成", "小名"]
# 列表名稱 = [50, 20, 35, 15, 5, 10, 20]
# print(len(列表名稱))#列表的元素個數
# print(max(列表名稱))#列表的最大值
# print(min(列表名稱))#列表的最小值
# print(sum(列表名稱))#列表的總合
# print(列表名稱.count(20))#計算元素20出現的次數
# print(列表名稱.index(20))#元素20第一次出現的索引值
# 修改列表
# color = ["white", "block", "red"]
# color[1] = "black"  # 修改列表的值
# print(color)  #["white", "black", "red"]

#
# a = [1, 2, 3]
# b = a
# b[0] = 9
# print(a)  # [9, 2, 3]
# a = 1
# b = a
# b = 9
# print(a)  # 1

# 判斷式
# if 判斷式: # 需要打冒號(:)
#    執行式 # 需要縮排(按Tab)
# a = 59
# if a < 60:
#    print("不及格!!")
#    print("要加油喔!")

# if 判斷式:
#    執行式
# else:
#    執行式
# a = 7
# if a == 6:
#    print("六六大順")
# else:
#    print("要小心喔")

# if 判斷式:
#    執行式
# elif 判斷式:
#    執行式
# else:
#    執行式
# weather = "陰天"
# if weather == "晴天":
#     print("帶陽傘")
# elif weather == "陰天":
#     print("帶雨傘")
# elif weather == "雪天":
#     print("帶外套")
# else:
#     print("不出門")
# rain = True
# wind = True
# if rain == True and wind == True:
#     print("不出門")
# rain = False
# wind = False
# if not rain and not wind:
#     print("出門")
# rain = True
# wind = False
# if rain == True and wind == True:
#     print("不出門")
# elif rain == True or wind == True:
#     print("帶傘出門")
# else:
#     print("開心出門")

# a = 1
# b = 1
# result = 0
# 解一
# if a == 0 and b == 0 and result == 0:
#     print("AND")
#     print("OR")
#     print("XOR")
# elif a == 0 and b == 0 and result == 1:
#     print("NOR")
# elif a == 1 and b == 1 and result == 0:
#     print("XOR")
#     print("NOR")
# elif a == 1 and b == 1 and result == 1:
#     print("AND")
#     print("OR")
# elif (a == 1 or b == 1) and result == 0:
#     print("AND")
#     print("NOR")
# elif (a == 1 or b == 1) and result == 1:
#     print("OR")
#     print("XOR")
# 解二
# if (a and b) == result:
#     print("AND")
# if (a or b) == result:
#     print("OR")
# if (a == b) != result:
#     print("XOR")
# if (a or b) != result:
#     print("NOR")

# a = 45
# if a % 5 == 0 and a % 3 == 0:
#     print("Both")
# elif a % 5 == 0:
#     print("Only 5")
# elif a % 3 == 0:
#     print("Only 3")

# 變數 = input()  # input()預設接收為str

# a = input()  # 輸入123
# print(a)  # 123
# print(type(a))  # str

# score = (input("您這次段考考幾分:")
# print("您這次段考分數為%s" % (score))

# a = int(input())
# b = int(input())
# print("結果是%d" % (a + b))
# a = int(input())
# b = int(input())
# if a >= b:
#      print("可以買")
#  else:
#      print("錢不夠")

# name = []
# a = input("請輸入1號的姓名:")
# b = input("請輸入2號的姓名:")
# name.append(a)
# name.append(b)
# print(name)

# range(開始, 結束, 間隔)
# range(1, 10, 2)# 1 3 5 7 9
# range(開始, 結束)
# range(1, 10)# 1 2 3 4 5 6 7 8 9
# range(結束)
# range(5)# 0 1 2 3 4

# 迴圈

# for i in range(30):
#     print(1)# 輸出30個1

# for i in range(4):
#     print(i)# 輸出0 1 2 3

# for i in range(3):
#     a = i * 2
#     print(a)# 輸出0 2 4

# for i in range(3):
#     a = i * 2
# print(a)# (i最後等於的值)*2 輸出4

# a = int(input())
# for i in range(a + 1):
#     print(i, end=" ")

# a = int(input())
# b = int(input())
# sum = 0
# for i in range(a, b + 1):
#     sum += i
# print("%d加到%d等於%d" % (a, b, sum))

# fruit = ["蘋果", "香蕉", "鳳梨", "橘子"]
# for i in fruit:
#     print(i) #蘋果 香蕉 鳳梨 橘子

# fruit = ["蘋果", "香蕉", "鳳梨", "橘子"]
# for i in range(4):  # 0 1 2 3
#     print("第%d個水果是%s" % (i + 1, fruit[i])) # 第1個水果是蘋果 第2個水果是香蕉 第3個水果是鳳梨 第4個水果是橘子

# list1 = [1, 2, 3, 4]
# for i in range(len(list1)):
#     print(list1[i]) # 1 2 3 4

# for X in range(2, 7):
#     if X == 3:
#         break  # break跳出現在在的迴圈
#     print(X) # 2

# for X in range(2, 7):
#     if X == 3:
#         continue  # continue跳過這一輪並繼續執行下一輪
#     print(X) # 2 4 5 6

# 九九乘法表
# for i in range(1, 10):
#     for x in range(1, 10):
#         a = i * x
#         print("%dX%d=%d" % (i, x, a), end="\t")
#     print()

# for i in range(1, 6):
#     x = 5 - i
#     print(" " * x + "*" * i)
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 8, 2):
#     a = (7 - i) / 2
#     print(" " * int(a) + "*" * i)
# for x in range(1, 4):
#     b = 7 - (x * 2)
#     print(" " * x + "*" * int(b))
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


# num = 1
# while num < 4:
#     print(num)
#     num = num + 1
# # 1
# # 2
# # 3

# a = 0
# name = ["小熊", "菲比", "海綿寶寶", "派大星", "蟹老闆"]
# while a < len(name):
#     print(name[a])
#     a = a + 1
# #小熊
# #菲比
# #海綿寶寶
# #派大星
# #蟹老闆

# i = 1
# while i < 101:
#     if i % 2 != 0:
#         i = i + 1
#         continue
#     if i % 10 == 0:
#         print(i)
#         print()
#         i = i + 1
#         continue
#     print(i, end=" ")
#     i = i + 1

# 字典(dict)
# 以大括弧{}來表示dict的開始和結束
# 每一個元素都是一組key:value
# key:索引，value:值(每個索引對到一個值/值組)
# 字典={"索引":"值","索引":"值"}
# dict1={"a":"apple","b":"book"} # 2個元素
# dict2 = {}  # 空字典
# dict2["a"] = "apple" # 添加元素到空字典dict2
# dict2["b"] = "book" # 添加元素到空字典dict2
# print(dict2) # {'a': 'apple', 'b': 'book'}
# dict2["b"]="bee" # 更改索引"b"的值為"bee
# print(dict2) # {'a': 'apple', 'b': 'bee'}

# 建立預設字典
# seq = ["apple", "banana", "mango"]  # 預設索引(key)
# dict3 = dict.fromkeys(seq)  # 將seq內的值放入dict3的key
# print(dict3) # {'apple': None, 'banana': None, 'mango': None}
# dict3 = dict.fromkeys(seq, 10)  # dict3內所有值(value)填入10
# print(dict3) # {'apple': 10, 'banana': 10, 'mango': 10}

# dict4 = {"a": "apple", "b": "book"}
# print(dict4.keys())  # dict_keys(['a', 'b'])
# print(dict4.items())  # dict_items([('a', 'apple'), ('b', 'book')])

# import random
# ex = ["apple", "banana", "hana", "seed"]
# print(random.randint(0, 99))  # 隨機選取0到99間的整數
# print(random.randrange(0, 101, 2))  # 隨機選取0到100間的偶數
# print(random.choice(ex))  # 隨機一個元素
# print(random.sample(ex, 2))  # 隨機選取兩個元素
# random.shuffle(ex)  # 重新排列元素

# import random

# while True:
#     a = int(input("0:退出遊戲 1:剪刀 2:石頭 3:布"))
#     b = int(random.randint(1, 3))
#     if a == 0:
#         break
#     elif a == 1 and b == 1:
#         print("玩家出剪刀,電腦出剪刀")
#         print("平手")
#     elif a == 2 and b == 2:
#         print("玩家出石頭,電腦出石頭")
#         print("平手")
#     elif a == 3 and b == 3:
#         print("玩家出布,電腦出布")
#         print("平手")
#     elif a == 1 and b == 2:
#         print("玩家出剪刀,電腦出石頭")
#         print("電腦贏了")
#     elif a == 1 and b == 3:
#         print("玩家出剪刀,電腦出布")
#         print("玩家贏了")
#     elif a == 2 and b == 1:
#         print("玩家出石頭,電腦出剪刀")
#         print("玩家贏了")
#     elif a == 2 and b == 3:
#         print("玩家出石頭,電腦出布")
#         print("電腦贏了")
#     elif a == 3 and b == 1:
#         print("玩家出布,電腦出剪刀")
#         print("電腦贏了")
#     elif a == 3 and b == 2:
#         print("玩家出布,電腦出石頭")
#         print("玩家贏了")

# import random

# a = int(input("請輸入1-100中的整數:"))
# up = 100
# down = 1
# time = 1
# X = random.randint(1, 100)
# print(X)
# while True:
#     if time == 7 and a != X:
#         print("結束遊戲")
#         break
#     elif a < X:
#         down = a
#         time = time + 1
#         a = int(input("請輸入%d-%d中的整數:" % (a, up)))
#     elif X < a:
#         up = a
#         time = time + 1
#         a = int(input("請輸入%d-%d中的整數:" % (down, a)))
#     elif a == X:
#         print("猜中了!!")
#         break


# function

# x = 6  # 全域變數(global variable)

# def a():
#     x = 5  # 區域變數(local variable)
# a()
# print(x)  # 最後會顯示全域變數 6

# 全域變數不可直接在function裡面再次宣告
# length = 5  # 全域變數


# def calculate_square_area():
#     length = length + 1 # 這行會出錯


# calculate_square_area()


# 使用global，將函數內的area變成全域變數，可以在函數內部修改全域變數的值
# length = 5
# area = 100


# def calculate_square_area():
#     global area
#     area = length**2  # length是全域變數，修改全域變數area的值


# calculate_square_area()
# print(area) # 原本是100，被修改成25

# 無參數
# def hello():
#     print("helloworld")
# hello()  # helloworld

# def Dora():
#     print("Dora")


# for i in range(5):
#     Dora()


# 有參數
# def a(n1, n2):
#     print(n1 + n2)


# def b():
#     num1 = int(input())  # 5
#     num2 = int(input())  # 10
#     a(num1, num2)  # pass by value


# b()

# def getscore(a, b):
#     if b > 90:
#         print("%s好棒棒" % (a))
#     else:
#         print("%s再加油" % (a))


# name = "Sandy"
# score = 90
# getscore(name, score) # Sandy再加油

# def add():
#     a = int(input())
#     b = int(input())
#     return a + b # 返回值


# print(add())


# f = open("檔案名", "模式")

# w 寫檔案
# f = open("text.txt", "w")
# f.write("string\n")  # 不會自動換行，需用\n
# f.write("int")
# f.close()

# name = ["Sandy", "Hank", "Ben"]
# f = open("name.txt", "w")
# print(name, file=f)  # 用print會自動換行
# f.close()

# r 讀取
# read() 讀取所有內容，存入string
# f = open("text.txt", "r")
# a = f.read()
# print(a)
# f.close()
#
# string
# int
# float

# read(size) size為獨取字元數
# f = open("text.txt", "r")
# a = f.read(3)
# print(a)
# f.close() # str

# readlines() 以每行為單位存入list
# f = open("text.txt", "r")
# a = f.readlines()
# print(a)
# f.close() # ['string\n', 'int\n', 'float']

# readline() 每次只讀取一行
# f = open("text.txt", "r")
# for line in f.readlines(): # f.readlines() 可省略成 f
#   print(line)
# f.close()
# string
#
# int
#
# float

# f = open("text.txt", "r")
# a = f.readline()
# b = f.readline()
# print(a+b) # string
# int
# f.close()


# f = open("text.txt", "r")
# f.seek(1)
# a = f.readline()
# print(a) # tring
# f.close()

# f = open("text.txt", "r")
# print(f.read(1)) # s
# print(f.readline()) # tring
# print(f.tell()) # 8
# f.close()

# a 續寫功能
# f = open("text.txt", "a")
# f.write("\nfloat")
# f.close()

# f = open("text.txt", "r", encoding="utf-8")
# a = f.read()
# print(a)
# f.close()

# with open("text.txt", "r", encoding="utf-8") as f:
#     a = f.read()
#     print(a)

# a = input("請輸入檔名:")
# while True:
#     b = int(input("請選擇模式:1.讀檔並印出 2.清空內容並寫入 3.續寫 0.退出"))
#     if b == 1:
#         c = int(input("請選擇功能:1.列印全內容 2.列印字數 3.以列表形式列印 4.列印一行"))
#         if c == 1:
#             f = open("a", "r")
#             d = f.read()
#             print(d)
#             f.close()
#         elif c == 2:
#             h = int(input("請輸入想印出的字數:"))
#             f = open("a", "r")
#             d = f.read(h)
#             print(d)
#             f.close()
#         elif c == 3:
#             f = open("a", "r")
#             d = f.readlines()
#             print(d)
#             f.close()
#         elif c == 4:
#             f = open("a", "r")
#             for line in f:
#                 print(line)
#             f.close()
#     elif b == 2:
#         e = input("請輸入想儲存的內容:")
#         f = open("a", "w")
#         print(e, file=f)
#         f.close()
#         print("儲存完畢")
#     elif b == 3:
#         g = input("請輸入想續寫的內容:")
#         f = open("a", "a")
#         print(g, file=f)
#         f.close()
#         print("儲存完畢")
#     elif b == 0:
#         break

# 以列表格式印出
# import csv

# f = open("score.csv", "r", encoding="utf-8-sig")
# for line in csv.reader(f):
#     print(line)
# f.close()

# 以字典格式印出
# import csv


# f = open("score.csv", "r", encoding="utf-8-sig")
# for line in csv.DictReader(f):
#     print(line)
# f.close()

# 指定項目並以字典格式印出
# import csv

# f = open("score.csv", "r", encoding="utf-8-sig")
# for row in csv.DictReader(f):
#     print(row["Name"], row["Age"])
# f.close()

# 指定某個項目並以字典格式印出
# import csv

# f = open("score.csv", "r", encoding="utf-8-sig")
# for row in csv.DictReader(f):
#     if row["Name"] == "小黃":
#         print(row)
# f.close()

# csv 列表 w 寫檔案
# import csv
#
# f = open("demo.csv", "w", newline="", encoding="utf-8")
# csvWriter = csv.writer(f)
# csvWriter.writerow(["名字", "學號", "分數"])
# csvWriter.writerow(["小黃", "F68599258", "50"])
# csvWriter.writerow(["小黑", "F78052643", "25"])
# csvWriter.writerow(["小粉", "F85049562", "56"])
# csvWriter.writerow(["小白", "F74052866", "89"])
# f.close()

# csv 列表 a 續寫
# import csv
#
# f = open("demo.csv", "a", newline="", encoding="utf-8")
# csvWriter = csv.writer(f)
# csvWriter.writerow(["小蘭", "F78496863", "33"])
# f.close()

# csv 字典 a 續寫
# import csv
#
# f = open("demo.csv", "w", newline="", encoding="utf-8")
# fields = ["名字", "學號", "分數"]
# csvWriter = csv.DictWriter(f, fieldnames=fields)
# csvWriter.writeheader()  # 寫入標題
# csvWriter.writerow({"名字": "小黃", "學號": "F68599258", "分數": "50"})
# csvWriter.writerow({"名字": "小黑", "學號": "F78052643", "分數": "25"})
# csvWriter.writerow({"名字": "小粉", "學號": "F85049562", "分數": "56"})
# csvWriter.writerow({"名字": "小白", "學號": "F74052866", "分數": "89"})
# f.close()

# year = ["1998", "2001", "2000", "2003", "2009", "2013", "2017"]
# book = ["數位密碼", "大騙局", "天使與魔鬼", "達文西密碼", "失落的符號", "地獄", "起源"]


# str1 = "00032100321000"
# print(str1.strip("0"))  # 去掉頭尾的0
# 32100321
# str2 = "  run run  \n\n"
# print(str2.strip()) # 去除某字串頭尾指定的字串(預設刪除空格和換行符號)
# run run
# f = open("name.txt", "r")
# a = f.readlines()
# for i in range(len(a)):
#     a[i] = a[i].strip() # 前面三行也可省略成 a = [i.strip() for i in f.readlines()]
# print(a)
# f.close()  # ['Sandy', 'Hank', 'Ben']

# import csv

# f = open("menu.txt", "r", encoding="utf-8")
# X = [i.strip() for i in f.readlines()]
# print(X)
# f.close()
# X = dict.fromkeys(X, 0)
# Y = []
# Z = []
# while True:
#     a = input("請輸入學生姓名(或輸入q結束)")
#     if a != "q":
#         if a in Y:
#             print("⚠️這位學生以經點過餐了!")
#             continue
#         Y.append(a)
#         b = input("請輸入餐點名稱:")
#         if b in X.keys():
#             print("✅%s 點了 「%s」" % (a, b))
#             X[b] += 1
#         else:
#             print("❌餐點不再菜單中，請重新輸入")
#             Y.remove(a)
#     elif a == "q":
#         print("📦餐點統計已完成，結果已登入order_summary.csv")
#         f = open("order_summary.csv", "w", newline="", encoding="utf-8")
#         csvWriter = csv.writer(f)
#         csvWriter.writerow(["餐點", "數量"])
#         v = 0
#         for c in X:
#             csvWriter.writerow([c, X[c]])
#         f.close()
#         break


# 例外處理:在發生錯誤時可以進行對應的動作
#
# NameError 使用沒有被定義的對象
# IndexError 索引值超過內容大小
# TypeError type錯誤
# SyntaxError Python語法規則輸入錯誤
# ValueError 傳入值錯誤
# KeyError 字典key鍵發生錯誤
# ZeroDivisionError 除以0

# try:
#     print(a)
# except NameError:
#     print("這個變數還沒被宣告")

# try:  # 使用try來測試內容是否正確
#     number = int(input("請輸入一個字"))
#     print(number)
# except:  # 如果try的內容發生錯誤，就執行except的內容
#     pass  # 略過
# else:
#     print("城市沒有錯誤!繼續執行")  # 完全沒錯才會執行這行
# finally:
#     print("管他有沒有錯，繼續執行") # 不論有沒有錯都會執行

# from datetime import datetime
# %Y 年分(西元)
# %m 月份(兩位數)
# %d 日(兩位數)
# %H 小時(24小時制)
# %M 分鐘
# %S 秒
# a = input("請輸入日期，格式是西元-月-日")
# try:
#     datetime.strptime(a, "%Y-%m-%d")  # 用來比對前面字串是否符合後面規定的日期格式
# except:
#     print("請輸入正確日期格式")

# import csv

# f = open("attendance.csv", "w", encoding="utf-8")
# f.close()
# f = open("report.csv", "w", newline="", encoding="utf-8")
# csvWriter = csv.writer(f)
# csvWriter.writerow(["學生", "出席次數", "缺席次數", "出席率(%)"])
# f.close()
# from datetime import datetime

# a = input("請輸入今天的日期(格式:YYYY-MM-DD):")
# try:
#     datetime.strptime(a, "%Y-%m-%d")
#     f = open("students.txt", "r", encoding="utf-8")
#     student = f.readlines()
#     f.close()

#     while True:
#         for i in student:
#             Z = input("%s 是否出席?(y/n):" % (i.strip()))
#             if Z == "y":
#                 f = open("attendance.csv", "a", newline="", encoding="utf-8")
#                 csvWriter = csv.writer(f)
#                 csvWriter.writerow([a, i.strip(), "出席"])
#                 f.close()
#                 f = open("report.csv", "a", newline="", encoding="utf-8")
#                 csvWriter = csv.writer(f)
#                 csvWriter.writerow([i.strip(), 1, 0, 100.0])
#                 f.close()

#             elif Z == "n":
#                 f = open("attendance.csv", "a", newline="", encoding="utf-8")
#                 csvWriter = csv.writer(f)
#                 csvWriter.writerow([a, i.strip(), "缺席"])
#                 f.close()
#                 f = open("report.csv", "a", newline="", encoding="utf-8")
#                 csvWriter = csv.writer(f)
#                 csvWriter.writerow([i.strip(), 0, 1, 0.0])
#                 f.close()
#         print("✅點名資料已储存")
#         b = input("是否要產生出席率分析報表?(y/n)")
#         if b == "y":
#             print("報表已儲存到 report.csv")
#             break
# except:
#     print("❌日期格式錯誤")


# set 集合
# 集合名稱 = {元素1, 元素2}
# 集合名稱 = set() # 空集合
# 集合是一種沒有順序、可以更改內容但內容不能重複的資料結構
# 像是只有key鍵，沒有value的字典
# a = {0, 1, 2, 3, "a", "b", False}  # False 等同於0，所以只保留0
# print(a)  # {0, 1, 2, 3, "a", "b"}

# s = {"apple", "banana", "banana"}
# print(s)  # {'apple', 'banana'}

# 可過濾重複資料再轉回列表
# 或把兩群資料放到不同集合中，觀察交集

# 新增單一元素
# fruits = {"apple", "banana"}
# fruits.add("kiwi")
# print(fruits)  # {"apple", "banana", "kiwi"} (若加入的元素已存在，則集合不變)

# 新增多個元素
# fruits = {"apple"}
# fruits.update(["banana","orange"]) # 裡面可以放list或set
# print(fruits) # {"apple", "banana", "orange"}

# 刪除元素
# fruits = {"apple", "banana"}
# fruits.remove("apple")
# print(fruits)  # {"banana"}
# 如果元素不存在，會出現錯誤(KeyError)
# fruits.remove("kiwi")  # 會報錯

# 刪除指定元素
# fruits = {"apple", "banana"}
# 如果元素不存在，不會報錯
# fruits.discard("kiwi")
# print(fruits)  # {"apple", "banana"}

# fruits = {"apple", "banana", "orange"}
# for i in fruits:
#     print(i) # 隨機順序印出三個元素
# set是無序集合，他的設計本來就不保證元素的順序
# 使用for i in list(fruits): 也是無序集合
# 需使用sorted()
# fruits = {"apple", "banana", "orange"}
# for i in sorted(fruits):
#     print(i) # sorted()方法將可迭代物件轉成由小到大排序後的列表，可以確保每次輸出的順序都是一樣的
# 可迭代物件有 : 列表、字典、元組、集合、字串

# fruits = ["apple", "banana", "orange"]
# print(fruits.sort())  # None (直接更改原列表，需在印出原列表才能得到更改後的結果)
# print(sorted(fruits))  # ['apple', 'banana', 'orange'] (直接複製一份更改後的列表)

# a = "b b   b"
# a = a.split()  # split() 預設是用空白當作分隔符號，會回傳列表
# print(a) #['b', 'b', 'b']

# a = "b:b:b"
# a = a.split(":") # split(":") 用冒號當作分隔符號
# print(a) #['b', 'b', 'b']

# Y = []
# a = input().split()  # 輸入1 2 3 4 5
# for i in a:
#     Y.append(int(i))
# print(Y)  # 輸出[1, 2, 3, 4, 5]

# map()方法
# map(函式名稱,可迭代物件)

# a = ["1", "2", "3"]
# b = list(map(int, a))  # 需用list()把map物件轉成列表
# # map()方法用來對可迭代物件的每一個元素逐一套用某個函式
# # 會回傳map物件
# # 需用list()把map物件轉成列表才能看到結果
# print(b)  # [1, 2, 3]

# a = list(map(int, input().split()))
# print(a)

# nums = [1, 2, 3, 4]
# def square(x):
#     return x * x
# result = map(square, nums)
# print(list(result))  # [1, 4, 9, 16]

# def add_num(a, b):
#     return a + b
# number1 = list(map(int, input().split())) # 輸入1 1 1
# number2 = list(map(int, input().split())) # 輸入2 2 2
# result = list(map(add_num, number1, number2))
# print(result)  # [3, 3, 3]

# h = list(map(float, input().split()))
# w = list(map(float, input().split()))
# def BMI(h, w):
#     return round(w / (h**2), 2)
# result = list(map(BMI, h, w))
# print(result)

# a = set(input().split())
# a = list(map(int, a))
# print(sorted(a))

# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}
# # 交集{a and b}
# print(a.intersection(b))  # {3,4,5}
# print(a & b)  # {3,4,5}

# # 聯集{a or b}
# print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7}
# print(a | b)  # {1, 2, 3, 4, 5, 6, 7}

# # 差集{a 減 (a and b)}
# print(a.difference(b))  # {1, 2}
# print(a - b)  # {1, 2}


# # 對稱差集{(a or b)減(a and b)}
# print(a.symmetric_difference(b))  # {1, 2, 6, 7}
# print(a ^ b) # {1, 2, 6, 7}

# 數字遊戲
# n = int(input())
# num = []
# for i in range(n):
#     N = int(input())
#     num.append(N)
# for i in range(n):
#     N = num[i]
#     Z = False
#     for b in range(100000):
#         a = N * b
#         if a > 100000:
#             continue
#         X = str(a) + str(b)
#         if len(set(X)) == 10:
#             print("%s / %s = %s" % (a, b, N))
#             Z = True
#         elif len(set(X + "0")) == 10 and len(set(str(b) + "0")) == 5:

#             print("%s / 0%s = %s" % (a, b, N))
#             Z = True
#     if not Z:
#         print("There are no any solutions for %s" % (N))

# Python兩種序列結構
# 元組(tuple)
# 列表(list)
# 兩種都可將任一種物件最為他們的元素
# a = ("apple", "banana", "orange", "grape")
# b = ("apple",)
# print(type(a))  # tuple
# print(type(b))  # tuple
### tuple與列表差異
# tuple 只要建立了就不能修改內容
# tuple 使用小括號，串列 list 使用中括號
# 如果 tuple 裡只有一個元素，後方必須加上逗號(多個元素就不用)

### 使用 tuple 的好處
# 讀取速度比串列快
# 占用的空間比較少
# 資料更安全(因為無法修改)

# 使用變數讀取 tuple
# 因為 tuple 可以一次賦予多個變數內容，透過這個方法可以一次將項目丟給不同的變數
# 接著只要讀取變數，就能讀取對應內容
# 使用此方法時，變數的數量要等於 tuple 的內容數量
# fruit = ("apple", "banana", "orange", "grape")
# a, b, c, d = fruit
# print(a) # apple
# print(b) # banana
# print(c) # orange
# print(d) # grape

# 使用索引讀取 tuple
# 在 tuple 裡每個項目都有自己的索引值 offset
# 指定 offset 就能讀取該資料的內容
# fruit = ("apple", "banana", "orange", "grape")
# print(fruit[0])  # apple
# print(fruit[1])  # banana
# print(fruit[2])  # orange
# print(fruit[3])  # grape

# a = ["apple", "banana", "orange", "grap"]
# b = tuple(a)  # 將列表轉成 tuple
# print(type(b))  # tuple

# 結合 tuple
# t1 = ("apple", "banana", "orange")
# t2 = ("grap", "pineapple")
# t = t1 + t2
# print(t)  # ('apple', 'banana', 'orange', 'grap', 'pineapple')

# 重複 tuple
# a = ("apple",)
# b = a * 3
# print(b)  # ('apple', 'apple', 'apple')

# 強制修改 tuple
# a = ("apple", "banana")
# b = list(a)
# b.append("orange")
# a = tuple(b)
# print(a) # ('apple', 'banana', 'orange')

# 檢查元素
# langs = ("Python", "Java", "C++")
# print("Python" in langs)  # True
