import numpy as np # 習慣上用 np 當縮寫
# print(np.array([1,2,3])+np.array([5,6,7])) # [ 6  8 10] 
# print([1,2,3]+[5,6,7]) # [1, 2, 3, 5, 6, 7]


# import numpy as np
# b=np.array([[1,2,3],[4,5,6]])
# print(b) # [[1 2 3] [4 5 6]]
# print("形狀 shape:", b.shape) # (2, 3) 代表 2 列 3 行
# print("維度 ndim:", b.ndim) # 2 代表 2 維
# print("元素型態 dtype:", b.dtype) # int64 代表 64 位元
# print("元素總數 size:", b.size) # 6 代表有 6 個元素

# 快速建立陣列
# print(np.zeros((2,3))) # 建立 2 X 3 行元素全為 0 的陣列
# print(np.ones((3,3))) # 建立 3 X 3 行元素全為 1 的陣列
# print(np.arange(0,10,2)) # [0 2 4 6 8]
# print(np.linspace(0,1,5)) # [0.   0.25 0.5  0.75 1.  ]
# np.linspace()產生等差數列的方法

# Numpy不需要使用for迴圈就可以對陣列進行運算
# x = np.array([1,2,3])
# y = np.array([10,20,30])
# print(x+y) # [11 22 33]
# print(x*y) # [10 40 90]
# print(x**2) # [1 4 9]
# print(x+10) # [11 12 13]
# print(x@y) # 矩陣乘法 140

# a=np.arange(5,25,5)
# print(a*3-2)

# arr = np.array([[1,2,3,4,5,6]])
# newarr = arr.reshape(2,3) # 重新塑形為 2 列 3 行 (roll, column)
# print(newarr) # [[1 2 3]
#               #  [4 5 6]]
#記得轉換前後的元素個數要相同，否則會報錯

# a=np.arange(1,13).reshape(3,4) 
# print(a) 
# print("形狀 shape:", a.shape)

# a=input()
# if len(a.split(" "))%2!=0:
#     a=list(map(int,a.split(" ")))
#     a.append(0)
# else:
#     a=list(map(int,a.split(" ")))
# A=np.array(a).reshape(2,int(len(a)/2))
# print(A)

# a=input()
# a=a.split(" ")
# if len(a)==6:
#     a=list(map(int,a))
#     A=np.array(a).reshape(2,3)
#     print(A)
# else:
#     print("元素數量不符合 6 個，無法重組")

# scores = np.array([55,80,72,90,45,60,100,85,66])
# 1. 基本統計
# print("總和 sum:", np.sum(scores))
# print("平均 mean:", np.mean(scores))
# print("中位數 median:", np.median(scores)) 
# print("標準差 std:", np.std(scores))
# print("變異數 var:", np.var(scores))
# # 2. 最大 / 最小
# print("最高分 max:", np.max(scores))
# print("最低分 min:", np.min(scores))
# # 3. 其他常用數學函數
# print("每個分數的平方:", np.square(scores))
# print("每個分數開根號:", np.sqrt(scores))
# print("每個分數的 log (自然對數):", np.log(scores)) 

# prices = [120,350,50,200]
# quantities = [2,1,5,3]
# P=np.array(prices)
# Q=np.array(quantities)
# if np.sum(P*Q)>=1000:
#     print("個商品小計: ", P*Q)
#     print("符合滿額折扣 ! 最終應付金額: ", np.sum(P*Q)*0.9)

# a=np.array([85,92,78,60,45,90])
# print("全班平均分數:", np.mean(a))
# for i ,u in enumerate(a,start=1):
#     if u>=60:
#         print("Student %d: %d (Pass)"%(i,u))
#     else:
#         print("Student %d: %d (Fail)"%(i,u))

# a=np.arange(1.,10.,2.)
# print("原始數值:", a)
# print("開根號結果:", np.sqrt(a).round(2))

# scores = np.array([82,90,55,78,65,95,40,88])
# print("平均值:",np.mean(scores))
# print("最高分:",np.max(scores))
# print("最低分:",np.min(scores))
# print("標準差:",np.std(scores).round(2))

# N=int(input())
# A=[]
# a=[]
# for i in range(1,N+1):
#     a=[]
#     for j in range(1,N+1):
#         a.append(i*j)
#     A.append(a)
# A=np.array(A).reshape(-1)
# print(A)
# print(np.sum(A))
# print(np.mean(A))







