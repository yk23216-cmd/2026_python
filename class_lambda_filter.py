# lambda 匿名函式

# 格式
# lambda 參數1,參數2, ... : 表達式

# 無參數
# f = lambda: "Hello, world!"
# print(f())  # Hello,world!
# 也可簡化成
# print((lambda: "Hello, world!")()) # Hello,world!

# 一個參數
# x = lambda a: a + 10
# print(x(5)) # 15
# 也可簡化成
# print((lambda a: a + 10)(5)) # 15

# 多個參數
# x = lambda a, b: a * b # 使用逗號隔開
# print(x(5, 6)) # 30

# 先定義匿名函數，再呼叫
# print((lambda: "Hello, world!")())  # Hello, world!
# 不在匿名函式外加括號就無法成功呼叫
# print(lambda: "Hello, world!"())  # 呼叫失敗

# 特性
# 不需要定義名稱
# 只能有一函式
# 執行完成後自動回傳結果


# def x(n):
#     a = [i**2 for i in range(1, n + 1) if i % 2 == 0]
#     # list comprehension 列表生成式 (要用中括號包起來) 是可以快速產生列表的方法
#     # 可把for迴圈和if判斷式都濃縮在一行
#     # 先做for和if然後才進行最前面的運算
#     return a
# y = lambda n: [i**2 for i in range(1, n + 1) if i % 2 == 0]
# # 計算後回傳平方數列表
# print(x(5))  # [4, 16]
# print(y(5))  # [4, 16]


# def y(n):
#     if n < 10:
#         return True
#     else:
#         return False
# x = lambda n: True if n < 10 else False
# # 判斷是否小於10，回傳True或False
# print(x(5))  # True
# print(y(5))  # True

# n = int(input())
# l = lambda: [len(input()) for i in range(n)]
# print(l())


# 列表生成式
# 透過簡化版的for迴圈對已有的所有元素進行處理或創建新列表
# 列表名稱 = [對元素做得處理for元素in可迭代物件]
# 可迭代物件有 : 列表、字典、元組、集合、字串、range


# num = [1, 3, 5, 7]
# new_num = []
# for i in num:
#     new_num.append(i * 2)
# print(new_num)  # [2, 6, 10, 14]

# 列表生成式
# new_num = [i * 2 for i in [1, 3, 5, 7]]
# print(new_num) # [2, 6, 10, 14]

# a = input()
# n = [i.lower() for i in a]
# print(n)

# 先使用for迴圈取出元素
# 再透過if條件篩選元素
# 最後對篩選出的元素做處裡
# 列表名稱 = [對元素做的處理 for 元素 in 可迭代物件 if 條件]

# numbers = []
# for i in range(5, 11):
#     if i % 2 == 0:
#         numbers.append(i * 2)
# print(numbers)  # [12, 16, 20]

# 列表生成式
# numbers = [i * 2 for i in range(5, 11) if i % 2 == 0]
# print(numbers)  # [12, 16, 20]

# 和map結合
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = map(lambda x: x * x, a)
# print(list(b))
# # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# # 因為map完會回傳map物件，所以需要再轉回list


# 用sorted排序二維list
# a = [[1,2],[4,3],[5,1],[9,2],[3,7]]
# b = sorted(a, key = lambda x:x[1]) # 指定用每個元素的第二個數字排序，相同則再取第一個數字排
# sorted(可迭代物件, key=函式)，會創一個新列表，所以不會影響原始列表
# key參數決定 用甚麼依據排序
# print(b)
# [[5,1], [1, 2], [9, 2], [4, 3], [3, 7]]
#
# 這個lambda函式會對列表a的每個元素x執行x[1]
# 每個x都是小列表，例如[1, 2]
# x[1]就是小列表的第二個元素
# 所以排序是依照每個子列表的第二個數字來排序

# a = [[1, 2], [4, 3], [5, 1], [9, 2], [3, 7]]  # 二維
# print(a[2][0])  # 5

# b = [[[1, 10], [2, 3]], [[4, 5], [3, 12]], [[5, 4], [4, 1]]]  # 三維
# print(b[0][0][1])

