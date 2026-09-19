# 1.自動順序對應
#print("我喜歡吃{}和{}。".format("蘋果","香蕉"))
# 輸出:我喜歡吃蘋果和香蕉。

# 2.指定索引與重複使用
#print("{1}今年{0}歲，{1}正在學習Python。".format(25,"小明"))
# 輸出:小明今年25歲，小明正在學習Python。
# (0對應25，1對應"小明")

# 使用關鍵字參數
#info = "名稱: {name}, 職業: {job}".format(job="教師",name="張三")
#print(info)                                      
# 輸出: 名稱: 張三, 職業: 教師


# 1. 使用 List 索引
#point = [10,20]
#print("X軸: {0[0]}, Y軸: {0[1]}".format(point)) # 0 代表第一個參數 point

# 2. 使用 Dictionary 鍵名 
#user = {"name": "Alex", "age": 18}
#print("{0[name]} 的年齡是 {0[age]} 歲。".format(user)) # 鍵名在中括號裡不用再加引號

# 3. 字典解包進階用法(常用)
#print("{name} 的年齡是 {age} 歲。".format(**user)) # 鍵名在大括號裡不用再加引號

#text = "Python"
# 靠左、靠右、置中，寬度為 10
#print("{:<10}".format(text))   # 'Python    '
#print("{:>10}".format(text))   # '    Python'
#print("{:^10}".format(text))   # '  Python  '

# 使用特電字元填補
#print("{:*^12}".format(text))  # '***Python***'

# 1. 小數點控制(f 代表浮點數，會自動四捨五入)
#print("{:.2f}".format(3.14159))  # 3.14

# 2. 加上千分位逗號
#print("{:,}".format(1234567890))  # 1,234,567,890

# 3. 百分比
#print("{:.1%}".format(0.856))  # 85.6%
# 自動乘以 100 並加上百分比符號，.1代表保留 1 位小數

# 4. 進位制轉換 (十進位 255)
#print("二進位:{:b}, 十六進位: {:x}".format(255, 255))
# 輸出: 二進位: 11111111, 十六進位: ff
# b (二進位), o(八進位), d(十進位), x(十六進位)

# name = "小明"
# age = 18
# 多個變數必須用小括號打包
# print("你好 %s，你今年%d歲。"%(name,age))
# 輸出: 你好 小明，你今年18歲。

# word = "Cat" 
# print("|%5s|"% word)  # 輸出: |  Cat| (靠右，補 2 空格)
# print("|%-5s|"% word) # 輸出: |Cat  | (靠左，補 2 空格)

# 1. 小數精度控制
#print("%.3f"%3.14159) # 輸出: "3.142"

# 2. 寬度與精度結合(總寬度 7，留 2 位小數)
#print("%7.2f"%3.14159) # 輸出: "   3.14"(包含小數點共 7 格)

# 3. 整數前置補零
#print("%04d"%7) # 輸出: "0007"

# import math
# # 印出系統內建的高精度圓周率
# print(f"內建圓周率:{math.pi}")
# r = 5.0
# circumference = 2 * math.pi * r
# print("半徑為 %d 的圓周長為 : %.4f  "%(r, circumference))

# import math 
# # 計算 2 的 3 次方
# result1 = math .pow(2,3)
# print(result1) # 輸出 8.0

# import math 
# # 目標 : 計算tan(45度)，正確答案是 1 
# angle = 45 
# # 錯誤示範 : 直接傳入角度
# print(f"tan(45) : {math.tan(angle)}")
# # 正確寫法 : 先將角度乘上 pi/180 轉換為弧度
# radian = angle*math.pi/180
# result2 = math.tan(radian)
# print(f"tan(45) : {result2:.1f}") # 輸出 : "tan(45) : 1.0"

# isdigit()判斷字串中的所有字元是否全部都是數字字元(0-9)
# 字串內至少要有一個字元，且所有字元都必須是數字，才會回傳True
# print("12345".isdigit()) # True
# print("123.45".isdigit()) # False (因為有小數點)
# print("-123".isdigit()) # False (因為有負號)
# print("12 3".isdigit()) # False (因為有空格)
# print("".isdigit()) # False

# startswith() 判斷字串是否已指定的字串作為開頭
# print("Python".startswith("py")) # False
# 檢查是否為常見的網頁協定開頭
# 這個方法可以傳入一個 Tuple，只要字串開頭符合 Tuple 中的其中一個元素，就會回傳 True 
# url = "https://google.com"
# print(url.startswith(("hppts://", "https://"))) # True

# 指定搜尋範圍(切片限制)
# str.startswith(prefix, start, end)
# text = "I love Python"
# print(text.startswith("love", 2)) # True 從索引 2 開始檢查，是否以 "love" 開頭

# 判斷字串中的所有字元是否全部都是英文字母，並回傳布林值
# 在 Python 3 中，.isalpha()的定義是基於 Unicode 字符集的
# 所有中文、法文等各國語言的書寫文字元，在 .isalpha() 下，通通會回傳 True
# print("Hello".isalpha()) # True
# print("中文".isalpha()) # True

# 英文字母檢查器
# user_input = input("請輸入字串:")
# is_pure_english = True
# if len(user_input)==0:
#     is_pure_english=False
# else:
#     for char in user_input:
#         # 檢查字串中每一個字元必須在'a'-'z' 或 'A'-'Z' 的範圍內
#         if not(char.isalpha()and(('a'<= char <='z')or('A'<=char<='Z'))):
#             is_pure_english = False
#             break
# if is_pure_english:
#     print("純英文字串")
# else:
#     print("含有非英文")

# 判斷字串是否已指定的字串做結尾，並回傳布林值
# 同樣支援 Tuple 多重匹配，以及限制搜尋範圍的參數(suffix,start,end)
# filename = "report.docx"
# 檢查是否為 Word 檔案
# print(filename.endswith(".docx")) # True
# 結合Tuple
# image = "photo.JPEG"
# 注意大小寫敏感，會回傳 False，實務上會先用 .lower() 轉小寫
# print(image.endswith((".jpg",".png",".jpeg"))) # False

# def factorial(n):
#     # 1. 終止條件 (Base Case)
#     if n==1:
#         return 1
#     # 2. 遞迴步驟 (Recursive Step)
#     return n*factorial(n-1)
# print(factorial(5)) # 輸出 120

# s="hello"
# print(s[-1]) # 輸出: "o" (只拿最後一個字)
# print(s[1:-1]) # 輸出: "ell" (拿範圍中的字)

# ord() 是 Python 中用來查詢字元的 字元碼(Unicode / ASCII 碼)的內建函式
# 字元 : 長度唯一的字串
# print(ord("A")) # 輸出: 65
# print(ord("a")) # 輸出: 97
# print(ord("0")) # 輸出: 48
# print(ord(2)) # ord() 專門用來處理 "字元" ，所以這一行會報錯
# 搭配 chr() 做反轉
# code = ord("B") # 66
# print(chr(code)) # 輸出: "B"
# 實用技巧:判斷大小寫相差32
# diff = ord("a")-ord("A") # 97 - 65 = 32

# .title() 讓每個單字開頭變大寫，其餘小寫
# n=input() # n=hellow wORLd
# print(n.title()) # 輸出: Hellow World

# 1. 基本全部替換
# text = "apple, apple, banana"
# new_text = text.replace("apple", "orange")
# print(new_text) # 輸出: orange, orange, banana
# 2. 使用 count 限制替換次數
# text2 = "cat cat cat cat"
# new_text2 = text2.replace("cat", "dog", 2)
# print(new_text2) # 輸出: dog dog cat cat
# 3.刪除特定字元(將舊字串換成空字串 "")
# text3 = "Hello World!"
# clean_text = text3.replace(" ", "")
# print(clean_text) # 輸出: HelloWorld!

# 1. 基本檢查
# print("PYTHON".isupper()) # 輸出: True
# print("Python".isupper()) # 輸出: False
# 2. 包含數字與符號(只要字母是大寫就過)
# print("CODE 2026!".isupper()) # 輸出: True

#　寫入資料，會覆蓋掉舊內容
# f = open("output.txt","w")
# f.write("Hello World\n")
# f.write("Second Line\n")
# f.close()

# 範例：　使用　writelines() 寫入列表
# lines = ["蘋果\n","香蕉\n","橘子\n"]
# f=open("fruit.txt","w",encoding="utf-8")
# f.writelines(lines) # 將列表每個元素寫入
# f.close()

# 在檔案末尾追加資料
# f=open("words.txt","a")
# f.write("New Entry\n")
# f.close()

# 範例: 連續追加多筆資料
# for i in range(3):
#     f=open("score.txt","a",encoding="utf-8")
#     f.write(f"第{i+1}次考試:{80+i*5}分\n")
#     f.close()
# 結果會累計三筆成績紀錄

# f= open("words.txt","r")
# 進行檔案讀寫操作
# read() 一次將整份檔案讀入為單一字串
# content = f.read()
# print(content)
# f.close()

# f= open("words.txt","r")
# 範例: 讀取指定字元數
# read(size) 讀取指定的 number 個字元
# first_10 = f.read(10)
# print(first_10)
# f.close()

# 範例: 讀取全部並存成列表
# f= open("words.txt","r")
# a=f.readlines() # 讀取所有行，並將每一行存成 List 中的元素
# print(a)
# f.close()

# 範例: 讀取一行
# f= open("words.txt","r")
# line1=f.readline() # 讀第一行(包含換行符號)
# line2=f.readline() # 讀第二行(包含換行符號)
# print(line1, end="")
# print(line2, end="")
# f.close()

# dict.get(key, default) 是Python 字典用來安全讀取資料的方法
# 當指定的 key 不存在時，它不會報錯崩潰，而是會回傳設定的預設值(default)
# person = {"name": "Alice", "age": 25 }
# 1. key 存在的狀況:正常取出對應的值
# name=person.get("name","未知")
# print(name) # 輸出: Alice
# 2. key 不存在的狀況:安全回傳指定的預設值
# gender=person.get("gender","不願透漏")
# print(gender)
# 3. 未指定預設值且 key 不存在:預設回傳 None
# height=person.get("height")
# print(height) # 輸出: 輸出: None

# f=open("words.txt","r",encoding="utf-8")
# f.tell():能知道目前指標的位置
# print(f.tell()) # 印出:0
# 讀取前五個字元("HELLO")
# text = f.read(5)
# print(text)
# 查看read(5)之後指標停在哪裡
# print(f.tell()) #　印出:5
# seek(位置)將指標強制移動到指定的位置
# f.seek(0) # 使用seek(0)強制將指標移回檔案最開頭
# print(f.tell()) # 印出: 0
# 重新讀取，又是從開頭開始讀出"HELLO"
# print(f.read(5))

# fruits = ["apple","banana","orange"]
# enumerate() 在走訪List時，能同時取得索引與元素
# for i,f in enumerate(fruits):
#     print("%s: %s"%(i,f))

# scores = [95, 88, 72]
# enumerate() 的start參數可以自訂編號
# for rank, score in enumerate(scores, start=1):
#     print(f"第 {rank} 名分數：{score}")

# r+ : 讀取+(覆蓋)寫入
# f=open("r_plus.txt","r+")
# 可讀可取，指標在開頭，寫入會從頭開始覆蓋(不是插入)
# f.write("sa")
# f.close()

# 範例:讀取內容後，從頭覆蓋部分文字
f=open("r_plus.txt","r+",encoding="utf-8")
content = f.read()
print("原始內容: ", content)
f.seek(0)
f.write("NEW")
f.close()






