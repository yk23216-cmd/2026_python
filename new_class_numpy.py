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

# prices=np.array([100,250,400,50])
# quantities=np.array([3,2,1,10])
# print("各商品總價:",prices*quantities)
# print("總消費金額:",np.sum(prices*quantities))

# 一維陣列取值
# 和 Python 列表類似，使用 "索引"
# arr = np.array([10,20,30,40,50])
# print(arr[0]) # 10
# print(arr[2]) # 30
# print(arr[-1]) # 取最後一個元素 50

# 二維陣列取值
# 格式 : arr[列索引, 行索引]
# mat = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(mat[0,0]) # 1
# print(mat[1,2]) # 6
# print(mat[2,-1]) # 9

# 切片
# 和 Python 列表類似，但可以同時對"列"和"行"取範圍
# arr = np.array([10,20,30,40,50])
# mat = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(arr[1:4])     # [20 30 40] 取索引 1~3 的元素
# print(mat[0:2,1:3]) # [[2 3]
#                     #  [5 6]]
# print(mat[:,0])     # [1 4 7] 
# print(mat[1,:])     # [4 5 6] 

# arr = np.array([12,25,38,41,55,63,70,84])
# print("切片結果:",arr[2:6])
# print("平均值:",np.mean(arr[2:6]))
# print("總和:",np.sum(arr[2:6]))

# N=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# n=N[1:3,1:3]
# print("右下角矩陣乘以10:\n",n*10)
# print("子矩陣總和:",np.sum(n*10))

# Z=np.zeros((4,4),dtype=int)
# Z[1:3,1:3]=1
# print(Z)
# print("矩陣總和:",np.sum(Z))

# def create_matrix(n):
#     N=np.zeros((n,n),dtype=int)
#     for i in range(n):
#         N[i,i]=i+1
#     print("Shape:",N.shape)
#     print("Sum:",np.sum(N))
#     print(N)
# n=int(input())
# create_matrix(n)

# np.eye(N,M = None, k = 0, dtype = float)
# N (必填) : 輸出矩陣的列數
# M (選填) : 輸出矩陣的行數，若未填則為預設 N X N 的方陣
# k (選填) : 對角線的偏移量
# dtype (選填) : 輸出矩陣的資料型態，預設為 float 也可以指定為 int
# 會建立單位矩陣或對角矩陣，對角線元素為 1 的二維陣列
# I = np.eye(3) # 3 X 3
# print(I)

# 建立 2 列 4 行 (2X4) 的矩陣
# rect_eye = np.eye(2,4,dtype=int)
# print(rect_eye) 

# k = 1 : 對角線往右上偏移一格
# upper = np.eye(4, k=1, dtype=int)
# print("k = 1 (右上偏移):")
# print(upper)

# k = -1 : 對角線往左下偏移一格
# lower = np.eye(4, k=-1, dtype=int)
# print("\nk = -1 (左下偏移):")
# print(lower)

# scores = np.array([55, 88, 92, 45, 73, 60, 100])
# 1. 產生布林遮罩 (Boolean Mask)
# pass_mask = scores >= 60
# print("及格遮罩:", pass_mask) # [False True True False True True True]
# 2. 使用遮罩取出元素
# passed_scores = scores[pass_mask]
# print("及格分數:", passed_scores) # [ 88  92  73  60 100]
# 3. 複合條件 (&:and、|:or、~:not)
# 篩選出 60 到 89 分之間的成績
# middle_mask = (scores >= 60) & (scores < 90)
# print("介於 60~89 分:", scores[middle_mask])
# 4. 遮罩修改值 (將不及格的補分至 60)
# scores[scores < 60] = 60
# print("補分後的成績:", scores) # [60 88 92 60 73 60 100]

# a = np.array([1, 2, 3, 4, 5])
# np.where 用來根據條件尋找陣列索引或進行條件判斷與數值替換
# np.where(條件, x, y)
# 符合條件回傳 x，否則 y
# result = np.where(a > 3, a, 0)
# print(result)        # [0 0 0 4 5]
# 取得符合條件的索引
# idx = np.where(a > 3)
# print(idx)           # (array([3, 4]),)

# a=int(input())
# b=int(input())
# X=np.arange(a,b+1)
# even_mask = X % 2 == 0
# even_numbers = X[even_mask]
# print("偶數:", even_numbers)
# odd_mask = X % 2 == 1
# odd_numbers = X[odd_mask]
# print("奇數:", odd_numbers)

# p=np.array([55, 80, 72, 90, 45, 60, 30, 100, 85, 66])
# print("平均: ",np.mean(p))
# print("及格: ",(p[p>=60]))
# print("最高: ",(np.max(p)))
# print("最低: ",(np.min(p)))
# print("60~80: ",(p[(p>=60)&(p<=80)]))

# a=input()
# b=input()
# a=np.array(a.split(" "), dtype=int)
# b=np.array(b.split(" "), dtype=int)
# print("各項金額: ",a*b)
# print("折抵後金額: ",np.where(a*b > 100, (a*b)-10, a*b))
# print("總應付金額: ",np.sum(np.where(a*b > 100, (a*b)-10, a*b)))

# a=input()
# a=np.array(a.split(" "), dtype=int)
# a=np.where((a%3==0)&(a%2!=0), a*10, a)
# print(a)

# a=input()
# a = np.array(a.split(" "), dtype=int)
# M=np.mean(a)
# a=np.where(a > M, 1, 0)
# a=a.reshape(3,3)
# print(a)

# a= input().title()
# a= np.array(a.split(" "))
# L=[]
# for i in a:
#     L.append(len(i))
# u = np.array(L)
# M_u = (4 <= u) & (u <= 8)
# n_a = a[M_u]
# print(n_a)

# a= input()
# a= np.array(a.split(" "), dtype=float)
# u=np.where(a>0,a**0.5,0)
# print(u)
# a[a<=0]=0.0
# a=a**0.5
# print(a)

# a = input()
# a = np.array(a.split(" "), dtype=float)
# u = np.where(a > 200, a*0.8, a)
# M=np.mean(a[a>0])
# print(round(M))
# u2= np.where(a <0, round(M), u)
# u2=np.reshape(u2, (4,4))
# print(u2)
# print("Row 0 Sum:", np.sum(u2[0,:]))
# print("Row 1 Sum:", np.sum(u2[1,:]))
# print("Row 2 Sum:", np.sum(u2[2,:]))
# print("Row 3 Sum:", np.sum(u2[3,:]))

# pswd = input()
# pswd = pswd.split(" ")
# P=np.array([8,1,1,1])
# k=[]
# for i in pswd:
#     L=len(i)
#     A=0
#     M=0
#     S=0
#     for u in i:
#         if 'A'<=u<='Z':
#             A+=1
#         if u in '0123456789':
#             M+=1
#         if 'A'<=u<='Z' and u not in '0123456789':
#             S+=1
#     K=[L, A, M, S]
#     k.append(K)
# k=np.array(k)
# k=k.reshape(4,4)
# for i in k:
#     if i[0]>=P[0] and i[1]>=P[1] and i[2]>=P[2] and i[3]>=P[3]:
#         print(i)

# f=open("fixed_log.txt","w")
# f.close()
# with open("server.log","r") as f:
#     lines=f.readlines()
#     u=[]
#     T=0
#     for i in lines:
#         i=i.strip().split(" ")
#         line=np.array(i)
#         if line[1]=="404" or line[1]=="500":
#             T+=1
#             u.append(int(line[2]))
#             M=sum(u)/T
#             if int(line[2])==max(u):
#                 line[2]=int(M)
#             with open("fixed_log.txt","a")as f:
#                 for i in line:
#                     f.write(str(i)+" ")
#                 f.write("\n")
#         else:
#             with open("fixed_log.txt","a")as f:
#                 for i in line:
#                     f.write(str(i)+" ")
#                 f.write("\n")
# print("Error Mean Time: %.1f"%(M))
# print("File fixed_log created successfully.")

# N=int(input())
# Z=np.ones((N,N),dtype=float)
# Z[1:-1,1:-1]=0
# print(Z)

# N=int(input())
# Z=np.zeros((N,N),dtype=float)
# for i in range(N):
#     Z[i,i]=1
#     Z[i,-i+N-1]=1
# print(Z)











