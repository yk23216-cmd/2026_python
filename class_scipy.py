# import scipy.constants as const
# math 模組僅提供基本的數學常數
# scipy.constants 專門針對科學計算，提供大量物理常數、數學常數以及單位換算係數

# 1. 取得數學與物理基本常數
# print("圓周率 pi:",const.pi)      # 3.141592653589793 
# print("光速 c:",const.c)          # 299792458.0
# print("普朗克常數 h:",const.h)     # 6.62607015e-34
# print("標準重力加速度 g:",const.g)  # 9.80665

# 2. 單位換算(時間、長度、壓力等)
# print("1 英吋等於多少米: ", const.inch)         # 0.0254
# print("1 磅等於多少公斤: ", const.lb)           # 0.45359236999999997
# print("1 大氣壓等於多少帕斯卡: ", const.atm)     # 101325.0

# 3. 實用計算 : 計算物體自由落體 5 秒的位移
# t = 5.0
# displacement = 0.5 * const.g * (t ** 2)
# print(f"自由落體{t}秒位移:{displacement:.2f}米") # 自由落體5.0秒位移:122.58米

# l=int(input())
# print("%7.2f cm"%(l*100*const.inch))

# M=eval(input())
# E=M*(const.c**2)
# print("%.3e J"%E)

# 
# from scipy.interpolate import interp1d
# 1. 建立已知數據點(x 與 y)
# x = np.array([0,1,2,3,4])
# y = np.array([0,2,4,6,8])

# 2. 建立線性插值函式
# f_linear = interp1d(x,y,kind="linear")

# 3. 預已知新數據點 x = 1.5 和 2.5 ， 並進行估算未知點 y
# x_new = np.array([1.5,2.5])
# y_new = f_linear(x_new)
# print("插值預測結果:",y_new)

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,2,4])
# y=np.array([10,30,20])
# fl=interp1d(x,y,kind="linear")
# n_x=float(input())
# n_y=fl(n_x)
# print("Y value: %.2f"%n_y)

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([1,2,3])
# y=np.array([5,15,25])
# fl=interp1d(x,y,kind="linear")
# x_n=np.linspace(1,3,5)
# y_n=fl(x_n)
# print("Sum of interpolated points: %.1f"%(np.sum(y_n)))

# import numpy as np
# from scipy.interpolate import interp1d
# with open("sensor.txt","r") as f:
#     t=np.array(list(map(float, f.readline().split(" "))))
#     v=np.array(list(map(float, f.readline().split(" "))))
#     fl=interp1d(t,v,kind="linear")
#     nt=2.5
#     nv=fl(nt)
#     print("Voltage: %.1f v"%(nv))

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,1,2,3])
# y=np.array([1,3,7,13])
# fl=interp1d(x,y,kind="linear")
# squ=lambda x:x*x
# n_x=np.array([0.5,1.5,2.5])
# n_y=squ(fl(n_x))
# print("Sum of Squares: %.2f"%(np.sum(n_y)))

# import numpy as np
# from scipy.interpolate import interp1d
# 1. 準備已知數據點
# x=np.array([0,1,2,3,4])
# y=np.array([0,1,8,27,64])
# 2. 建立三次樣條插值函式
# f_cubic=interp1d(x,y,kind="cubic")
# 3. 對查詢點進行插值
# queries=np.array([0.5,1.5,2.5,3.5])
# results=f_cubic(queries)
# print("三次樣條結果: ",results)

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,1,2,3])
# y=np.array([1,2,9,28])
# f=interp1d(x,y,kind="cubic")
# nx=1.5
# ny=f(nx)
# print("Cubic Interpolated: %.2f"%(ny))

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,1,2,4])
# y=np.array([0,2,4,0])
# f=interp1d(x,y,kind="linear")
# f2=interp1d(x,y,kind="cubic")
# nx=3
# ny=f(nx)
# ny2=f2(nx)
# Y=np.abs(ny-ny2)
# print("Difference: %.1f"%(Y))

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,1,2,3,4])
# y=np.array([2,3,5,7,11])
# f=interp1d(x,y,kind="cubic")
# xn=np.linspace(0,4,10)
# yn=f(xn)
# print("Max interpolated: %.2f"%(np.max(yn)))

# import numpy as np
# from scipy.interpolate import interp1d
# with open("temperature.txt","r",encoding="utf-8") as f:
#     line1=np.array(list(map(float,f.readline().strip().split(" "))))
#     line2=np.array(list(map(float,f.readline().strip().split(" "))))
#     f=interp1d(line1,line2,kind="cubic")
#     n1=10
#     n2=f(n1)
#     print("Hour 10 Temp: %.1f"%(n2))

# import numpy as np
# from scipy.interpolate import interp1d
# N=int(input())
# x=[]
# y=[]
# for i in range(N):
#     xy=input()
#     xy=xy.split(" ")
#     x.append(int(xy[0]))
#     y.append(int(xy[1]))
# xq=eval(input())
# if min(x)<=xq<=max(x):
#     x=np.array(x)
#     y=np.array(y)
#     f=interp1d(x,y,kind="cubic")
#     yn=f(xq)
#     print("Interpolated Y: %.3f"%(yn))
# else:
#     print("Out of bounds")

# import numpy as np
# from scipy.interpolate import interp1d
# n=(np.array([10,20,30,5,15,25,2,4,6])).reshape(3,3)
# x_old=np.array([0,1,2])
# y=(n[0],n[1],n[2])
# f=interp1d(x_old,y,kind="linear")
# xn=np.linspace(0,2,5)
# yn=f(xn)
# print(yn)

# import numpy as np
# from scipy.interpolate import interp1d
# 1. 準備好已知數據點
# x_known=np.array([0,2,4,6])
# y_known=np.array([10,20,50,40])
# 2. 建立最近臨插值函式
# f_nearest=interp1d(x_known,y_known,kind="nearest")
# 3. 查詢未知點
# print("x = 1.5 的最近鄰預測:",float(f_nearest(1.5)))
# x = 1.5 距離 2 最近 (對應原數據 y=20)
# print("x = 4.8 的最近鄰預測:",float(f_nearest(4.8)))
# x = 4.8 距離 4 最近 (對應原數據 y=50)

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([10,20,30])
# y=np.array([100,250,400])
# f=interp1d(x,y,kind="nearest")
# print("Predicted value: %d"%(f(22))) 

# import numpy as np
# from scipy.interpolate import interp1d
# x=np.array([0,10])
# y=np.array([100,200])
# f=interp1d(x,y,kind="nearest")
# f2=interp1d(x,y,kind="linear")
# print("Difference: %.1f"%(np.abs(f2(3)-f(3)))) 

# from scipy.optimize import minimize_scalar
# 1. 定義目標函數 f(x) = x**2 - 6x + 9
# def objective(x):
#     return x**2-6*x+9
# 2. 使用 minimize_scalar 尋找全域極小值
# res = minimize_scalar(objective)
# 3. 輸出最佳化結果
# print("極小值發生於 x = ",res.x)
# print("最小函數值 y = ",res.fun)

# from scipy.optimize import minimize_scalar
# def ob(x):
#     return (x-4)**2+10
# res=minimize_scalar(ob)
# print("x = %.2f, y = %.2f"%(res.x,res.fun))

# from scipy.optimize import minimize_scalar
# def f(x):
#     return x**3-3*x   # 有兩個極值點
# # 不指定範圍 : 可能找到任意局部最小值
# print("無範圍 : ",minimize_scalar(f).x)
# # 指定範圍 (0, 3) : 只在此區間找
# res = minimize_scalar(f,bounds=(0,3),method="bounded")
# print("限制範圍 (0, 3) : ",res.x)
# # 指定範圍 (-3, 0)
# res = minimize_scalar(f,bounds=(-3,0),method="bounded")
# print("限制範圍 (-3, 0) : ",res.x)

# from scipy.optimize import minimize_scalar
# def f(x):
#     return x**3-3*x+5
# res=minimize_scalar(f,bounds=(0,2),method="bounded")
# print("Min x = %.1f"%(res.x))

# from scipy.optimize import minimize_scalar
# def f(x):
#     return 3*(x**2)-60*x+500
# res=minimize_scalar(f)
# print("Optimal x: %d, Min Cost: %d"%(round(res.x),res.fun))

# from scipy.optimize import minimize_scalar
# import numpy as np
# def f(x):
#     return (np.abs(x-7.5))+3
# print("Minimum value: %.2f"%(minimize_scalar(f).fun))

# from scipy.optimize import minimize
# 把原本的單體變數問題用 minimize 重寫
# f(x) = x^2 - 6x + 9
# def ob(v):
#     # v 是陣列，即使只有一個變數 
#     x = v[0]
#     return x**2 - 6*x + 9
# minimize 需要初始猜測 x0 (用列表形式)
# res = minimize(ob, x0=[0])
# print("x = ",res.x)           # x =  [3.00000003]
# print("min = ",res.fun)       # min =  0.0
# print("成功?",res.success)    # 成功? True
# print("迭代次數 : ",res.nit)   # 迭代次數 :  2

# from scipy.optimize import minimize
# 雙變數 : f(x, y) = (x-1)^2 + (y+2)^2
# 最小值在 (1, -2)，最小值為 0
# def f(v):
#     x, y = v    # 直接把 v 拆成兩個變數 (python 解構方法)
#     return  (x-1)**2 + (y+2)**2
# res = minimize(f,x0=[0,0])  # 從 (0, 0) 出發
# print("最佳位置 : ",res.x)   # [ 0.99999998 -2.00000003]
# print("最小值 : ",res.fun)  # 1.1411716670850257e-15

# python 解構方法
# 原本方法(一個一個取)
# v = [1, 2]
# x=v[0]
# y=v[1]
# 解構方法(一行搞定)
# v = [1, 2]
# x, y = v
# print(x) # 1
# print(y) # 2

# from scipy.optimize import minimize
# f(x, y, z) = x^2 + y^2 + z^2 -2x - 4y - 6z
# 最小值在 (1, 2, 3)
# def f(v):
#     x,y,z=v
#     return x**2+y**2+z**2-2*x-4*y-6*z
# res = minimize(f,x0=[0,0,0])
# print("位置 : ",list(map(round,res.x))) # 位置 :  [1, 2, 3]
# print("最小值 : ",round(res.fun))       # 最小值 :  -14

# import numpy as np
# from scipy.optimize import minimize
# 這個函數有兩個局部最小值
# def f(x):
#     return x[0]**4 - 4 * x[0] **2 + x[0]
# 從不同初始點出發
# for x0 in [-2, 0, 2]:
#     res=minimize(f,x0=[x0])
#     print(f"從 x0 = {x0} 出發 => 找到 x = {res.x[0]:.4f}, f(x) = {res.fun:.4f}")
#     # 從 x0 = -2 出發 => 找到 x = -1.4730, f(x) = -5.4442
#     # 從 x0 = 0 出發 => 找到 x = -1.4730, f(x) = -5.4442
#     # 從 x0 = 2 出發 => 找到 x = 1.3470, f(x) = -2.6186

# from scipy.optimize import minimize
# def f(v):
#     x,y=v
#     return (x-5)**2+(y-3)**2
# res = minimize(f,x0=[0,0])
# print("x = ",res.x)
# print("min = ",res.fun)

# from scipy.optimize import minimize
# n=input()
# a,b,c=list(map(int,n.split(" ")))
# def f(v):
#     x,y=v
#     return (x-a)**2+(y-b)**2+c
# res=minimize(f,x0=[0,0])
# print("x = ",res.x)
# print("min = ",res.fun)

# from scipy.optimize import minimize
# import numpy as np
# def f(v):
#     x,y,z=v
#     return x**2+2*y**2+3*z**2-4*x-8*y-12*z
# res=minimize(f,x0=[0,0,0])
# print("x = ",np.round(res.x,4))
# print("min = %.4f"%(res.fun))

# from scipy.optimize import minimize_scalar
# 1. 這是原本的目標函數：開口向下的拋物線 f(x) = -(x - 5)^2 + 20
# 我們要找出它的「最高點」
# def original_func(x):
#     return - (x - 5)**2 + 20
# 2. 建立一個「顛倒版」的函數（把原本的函式乘以負號，讓最高點變成谷底）
# def negative_func(x):
#     return -original_func(x)
# 3. 用 minimize_scalar 去找出這個顛倒版函數的「最低點」
# res = minimize_scalar(negative_func)
# 4. 輸出結果
# print("最高點發生的 x 位置:", res.x)
# 注意：因為我們剛剛求的是負函數的最小值，所以要把 res.fun 加上負號變回來！
# print("最高點的最高數值 (y):", -res.fun)

# from scipy.optimize import minimize_scalar
# 1. 直接用 lambda 定義原本的函數，並在外面加上負號
# 這樣 minimize_scalar 找出來的就會直接是最低點，對應到原本函數的最高點
# res = minimize_scalar(lambda x: -(-(x - 5)**2 + 20))
# 2. 輸出結果
# print("最高點發生的 x 位置:", res.x)
# print("最高點的最高數值 (y):", -res.fun)

# from scipy.optimize import minimize_scalar
# res = minimize_scalar(lambda x : -(-(x-3)**2+25))
# print("最高點發生的 x 位置: ",res.x)
# print("最高點的最高數值(y): ",-res.fun)

# from scipy.optimize import minimize_scalar
# import numpy as np
# res = minimize_scalar(lambda x : -(np.sin(x)),bounds=(0,np.pi),method="bounded")
# print("Max x = %.3f, Max y = %.3f"%(res.x,-res.fun))





# import numpy as np
# from scipy import stats
# mat1=np.array([[10,20,30],[12,22,28],[11,21,29]])
# mat2 = np.array([[15,25,31],[14,24,30],[16, 26, 32]])
# n = mat1.shape[1]
# min_p=float("inf")
# u=-1
# for i in range(n):
#     col1 = mat1[:, i]
#     col2 = mat2[:, i]
#     t, p = stats.ttest_ind(col1, col2)
#     if p < min_p:
#         min_p = p
#         u = i
# print("Min p-value at index %d: %.4f" % (u, min_p))

# import numpy as np
# from scipy import stats
# 同一批人的前後測
# before = np.array([80, 85, 78, 90, 88])
# after  = np.array([78, 82, 76, 85, 84])
# 用配對 t 檢定（正確方式）
# t_rel, p_rel = stats.ttest_rel(before, after)
# print("配對 t 檢定 :", t_rel, p_rel)
# 用獨立 t 檢定（錯誤方式！忽略配對關係）
# t_ind, p_ind = stats.ttest_ind(before, after)
# print("獨立 t 檢定 :", t_ind, p_ind)
# 兩者結果不同！配對檢定通常 p 值更小（更靈敏）

# import numpy as np
# from scipy import stats
# b=np.array([82,75,90,68,77])
# a=np.array([78,74,85,65,76])
# t,p=stats.ttest_rel(b,a)
# print("p-value: %.4f"%(p))

# import numpy as np
# from scipy import stats
# b=np.array(input().split(" "),dtype=int)
# a=np.array(input().split(" "),dtype=int)
# t,p=stats.ttest_rel(b,a)
# if p < 0.05:
#     print("Significant Effect")
# else:
#     print("No Effect")

# import numpy as np
# from scipy import stats
# 1. 建立一個 2X2 的列聯表 (例如:性別與偏好某種產品的交叉統計)
# 橫排代表性別 (男、女)，縱排代表偏好 (喜歡、不喜歡)
# contingency_table = np.array([[30, 10],
#                               [20, 40]])
# 2. 進行卡方獨立檢定 
# 回傳值依序為:chi2 統計量, p-value, 自由度, 期望值矩陣
# chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
# print("卡方統計量:", chi2_stat)
# print("p 值:", p_value)
# if p_value < 0.05:
#     print("拒絕獨立假設: 兩個變數之間有顯著關聯")

# import numpy as np
# from scipy import stats
# n=np.array([[50,20],[30,40]])
# t,p,d,e=stats.chi2_contingency(n)
# print("p-value: %.4f"%(p))

# import numpy as np
# from scipy import stats
# u=input().split(" ")
# n=np.array([[u[0],u[1]],[u[2],u[3]]],dtype=int)
# t,p,d,e=stats.chi2_contingency(n)
# if p < 0.05:
#     print("Dependent")
# else:
#     print("Independent")

# import numpy as np
# from scipy import stats
# with open("multi_tests.txt","r")as f:
#     lines=f.readlines()
#     f.seek(0)
#     n=0
#     for i in range(len(lines)):
#         u=f.readline().strip().split(" ")
#         t,p=stats.ttest_1samp(np.array(list(map(float,u))),popmean=50)
#         if p < 0.05:
#             n+=i+1
#     print("Significant group indices sum: %d"%(n))
    
# import numpy as np
# from scipy import stats
# group1 = np.array([[10,20,30,],[12,21,35],[11,19,32]])
# group2 = np.array([[8,19,25],[9,18,27],[7,20,26]])
# with open("feature_report.txt","w")as f:
#     for i in range(group1.shape[1]):
#         t, p = stats.ttest_ind(group1[:, i], group2[:, i])
#         f.write("Feature %d | t: %.3f | p: %.3f\n" %(i+1, t, p))

# import numpy as np
# from scipy import stats
# bf=np.array(list(map(int,input().split(" "))))
# at=np.array(list(map(int,input().split(" "))))
# N=(at-bf)/bf*100
# t,p=stats.ttest_rel(bf,at)
# print("Mean Improvement Rate: %.2f%%, p-value: %.4f"%(np.mean(N),p))


import matplotlib.pyplot as plt # 匯入函式庫
x=[1,2,3,4,5]                   # 準備資料
y=[2,7,8,6,9]
plt.plot(x,y,"o",color="r")     # 繪製折線圖(點)
plt.show()
plt.plot(x,y,color="b")         # 只有線 
plt.show() 
plt.plot(x,y,"-o",color="g")    # 點和線
plt.show() 
plt.plot(x,y,"--o",color="y")    # 點和虛線
plt.show() 


   