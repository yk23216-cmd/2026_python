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

# from scipy.optimize import minimize_scalar
# res=minimize_scalar(lambda x: -(-2*x**2+40*x-50))
# print("Optimal discount x = %d, Max Revenue = %d"%(res.x,-res.fun))

# from scipy.optimize import minimize_scalar
# import numpy as np
# v=30
# g=9.80665
# res=minimize_scalar(lambda x: -(v**2*np.sin(2*x)/g))
# print("Best Angle: %.2f deg, Max Range: %.2f m"%(np.degrees(res.x),-res.fun))

# from scipy.optimize import root_scalar
# ===== 範例：解 x^2 - 4 = 0 =====
# 1. 定義方程式 f(x) = x^2 - 4 = 0
# def func(x):
#     return x ** 2 - 4
# 2. 在區間 [0, 5] 內尋找根
# brentq演算法，運作方式是透過不斷地「猜測數值」和「縮小搜尋區間」（疊代）
# 去找出讓 f(x) 趨近於 0 的點
# res = root_scalar(func, bracket=[0, 5], method='brentq')
# 3. 輸出方程式的根
# print("方程式的根:", round(res.root))  # 方程式的根: 1.999999999999977

# from scipy.optimize import root_scalar
# 1. 定義方程式 f(x) = x^3 - 2x - 5
# def target_func(x):
#     return x**3 - 2*x - 5
# 2. 使用 brentq 方法在 [2, 3] 內求根
# res = root_scalar(target_func, bracket=[2, 3], method='brentq')
# 3. 檢視詳細結果物件
# print("是否成功收斂:", res.converged)
# print("疊代次數:", res.iterations)
# print("求得的根 x =", res.root)
# print("驗證 f(root) =", target_func(res.root)) # 應該要非常接近 0

# import numpy as np
# from scipy.optimize import root_scalar
# 結合 lambda
# 在區間  [0,1] 內尋找 cos(x) = 0 的交點
# res = root_scalar(lambda x: np.cos(x)-x, bracket=[0, 1], method='brentq')
# print("交點 x =", res.root)

# import numpy as np
# from scipy.optimize import root_scalar
# res=root_scalar(lambda x: x**3-27, bracket=[1, 5], method='brentq')
# print("Root: %.3f"%(round(res.root, 3)))

# from scipy.optimize import root_scalar
# n=input().split(" ")
# res=root_scalar(lambda x: int(n[0])*x+int(n[1]), bracket=[-100, 100], method='brentq')
# print("Root: %.2f"%(round(res.root, 2)))

# import math
# from scipy.optimize import root_scalar
# res=root_scalar(lambda x: math.exp(x)-5, bracket=[1, 2], method='brentq')
# print("Root: %.3f"%(round(res.root, 3)))

# from scipy.optimize import minimize_scalar
# res=minimize_scalar(lambda x: -(100*x-x**2-(20*x+500)))
# print("Max Profit x = %d, Profit = %d"%(round(res.x),-res.fun))
# from scipy.optimize import root_scalar
# res2=root_scalar(lambda x: 100*x-x**2-(20*x-500), bracket=[0, 100], method='brentq')
# print("Break-even root = %.2f"%(round(res2.root, 2)))

# import math
# from scipy.optimize import root_scalar
# res=root_scalar(lambda x: x**2-4, bracket=[1, 3], method='brentq')
# res2=root_scalar(lambda x: x**3-8, bracket=[1, 3], method='brentq')
# res3=root_scalar(lambda x: math.log(x)-1, bracket=[2, 3], method='brentq')
# s=0
# for i in [res, res2, res3]:
#     if i.root >2:
#         s+=i.root
# print("Sum of filtered roots: %.2f"%(round(s, 2)))

# import numpy as np
# from scipy import stats
# 1. 準備一組學生的考試成績樣本
# scores = np.array([72, 75, 68, 80, 85, 78, 90, 74])
# 2. 進行單樣本 t 檢定，假設母體（或及格標準）平均數為 70
# 回傳值包含 t 統計量 (statistic) 與 p 值 (pvalue)
# t_stat, p_val = stats.ttest_1samp(scores, popmean=70)
# print("學生平均分:", scores.mean())
# print("t 統計量:", t_stat)
# print("p 值:", p_val)
# 3. 根據顯著水準 alpha = 0.05 進行假設檢定判斷
# if p_val < 0.05:
#     print("拒絕虛無假設：全班平均顯著異於 70 分")
# else:
#     print("接受虛無假設：與 70 分沒有顯著差異")

# import numpy as np
# from scipy import stats
# p=np.array([1.2,0.8,1.5,1.1,0.9,1.3])
# t_stat, p_val = stats.ttest_1samp(p, popmean=1)
# print("p-value: ", round(p_val, 4))

# import numpy as np
# from scipy import stats
# L=input().split(" ")
# p=np.array(list(map(int, L)))
# t_stat, p_val = stats.ttest_1samp(p, popmean=75)
# if p_val < 0.05 and p.mean() != 75:
#     print("Significant High")
# else:
#     print("Not Significant")

# import numpy as np
# from scipy import stats
# data = np.array([52.1, 49.8, 51.0, 50.5, 49.2, 50.8])
# t_stat, p_val = stats.ttest_1samp(data, popmean=50.0)
# res = np.array([t_stat, p_val])
# res_rounded = np.round(res, 3)
# print(res_rounded)

# import numpy as np
# from scipy import stats
# 1. 準備兩組獨立的樣本資料
# group_a = np.array([85, 90, 88, 92, 86, 89])
# group_b = np.array([75, 78, 72, 80, 76, 74])
# 2. 進行獨立樣本 t 檢定
# t_stat, p_val = stats.ttest_ind(group_a, group_b)
# print("獨立樣本 t 統計量:", t_stat)
# print("p 值:", p_val)
# 3. 判斷兩組表現是否有顯著差異
# if p_val < 0.05:
#     print("兩組之間存在顯著差異")

# import numpy as np
# from scipy import stats
# # 兩組樣本數不同也可以比較
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10,11,12])
# t,p=stats.ttest_ind(a,b)
# print(t,p)

# import numpy as np
# from scipy import stats
# a=np.array([45,48,50,47,49])
# b=np.array([40,42,41,44,43])
# t,p=stats.ttest_ind(a,b)
# print("p-value: %.4f"%(p))

# import numpy as np
# from scipy import stats
# L=input().split(" ")
# a=np.array(list(map(int,L)))
# L2=input().split(" ")
# b=np.array(list(map(float,L2)))
# t,p=stats.ttest_ind(a,b)
# if p<0.05 :
#     print("Difference")
# else:
#     print("No Difference")

# import numpy as np
# from scipy import stats
# 1. 準備同一群學生「特訓前」與「特訓後」的成績（具備嚴格配對關係）
# before = np.array([65, 70, 72, 68, 80, 75])
# after = np.array([78, 85, 80, 82, 88, 84])
# 2. 進行配對樣本 t 檢定
# t_stat, p_val = stats.ttest_rel(before, after)
# print("配對樣本 t 統計量:", t_stat)
# print("p 值:", p_val)
# if p_val < 0.05:
#     print("特訓前後有顯著進步差異")





# import matplotlib.pyplot as plt
# import numpy as np
# # 只給 y, x 自動用索引
# y = np.array([10,20,15,25])
# plt.plot(y) # x 自動為 [0, 1, 2, 3]
# plt.show() # 顯示圖表

# import matplotlib.pyplot as plt
# import numpy as np
# x= np.linspace(0,2*np.pi,100)
# 畫兩條線，各自給 label
# label 是寫在 plot() 裡，legend() 才會去讀它
# plt.plot(x,np.sin(x),label="sin(x)")
# plt.plot(x,np.cos(x),label="cos(x)")
# 加上標題與軸標籤
# plt.title("Sine and Cosine")
# plt.xlabel("x (radians)")
# plt.ylabel("y")
# plt.legend()  # 顯示圖例
# plt.grid()    # 顯示格線
# plt.show()    

# import matplotlib.pyplot as plt
# import numpy as np
# 設定中文字型(依作業系統選擇可用的)
# plt.rcParams["font.sans-serif"] = ["Microsoft YaHei","SimHei","Arial Unicode MS"]  
# 設定負號正常顯示(否則負號會變成方塊)
# plt.rcParams["axes.unicode_minus"] = False
# 之後畫圖就能使用中文了
# plt.plot([1,2,3],[-1,-2,-3])
# plt.title("測試中文範例")
# plt.show()

# plt.figure(figsize=寬, 高)) 控制圖表大小 (單位為英吋)
# 建立一個 8x5 英吋的圖表
# plt.figure(figsize=(8,5))
# plt.plot([1,2,3],[1,4,9])
# plt.title("自訂大小")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4,5])
# y = np.array([100,105,102,110,115])
# mi= np.argmax(y)
# mp=y[mi]
# mt=x[mi]
# plt.plot(x,y,color="r",marker="o")
# plt.title("Max Price: %d at Time %d"%(mp,mt))
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# with open("stock_trend.txt","r") as f:
#     f.seek(0)
#     t=np.array(f.readline().strip().split(" "),dtype=float)
#     v=np.array(f.readline().strip().split(" "),dtype=float)
#     print("Mean: %.2f"%np.mean(v))
#     print("Std: %.2f"%np.std(v))
#     plt.plot(t,v)
#     plt.show()
   
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-3,3,50)
# y=2*x**2-4*x+1
# plt.plot(x,y)
# mi=np.argmin(y)
# my=y[mi]
# mx=x[mi]
# print("Min Y: %.2f at X: %.2f"%(my,mx))
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(0,2*np.pi,50)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.plot(x,y1,label="sin")
# plt.plot(x,y2,label="cos")
# plt.legend()  
# print("Max Absolute Difference: %.3f"%((np.max(np.abs(y1-y2)))))
# plt.show()

# import matplotlib.pyplot as plt
# x=[1,2,4,6,8,1,2,9,3]
# y=[5,7,2,3,1,4,6,5,8]
# plt.title("Simple Plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.scatter(x,y,c="r") # 繪製散佈圖
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# 模擬 100 位學生的身高與體重
# np.random.seed(42)
# height=np.random.normal(170,10,100) # 平均 170，標準差 10
# weight=np.random.normal(65,8,100)   # 平均 65，標準差 8
# plt.scatter(height,weight)          # 畫散佈圖
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.title("Height vs Weight")
# plt.show()


# import numpy as np
# 1. 回傳單一隨機浮點數
# print(np.random.randn())
# 2. 建立一維陣列(如:包含五個隨機數)
# print(np.random.randn(5))
# 3. 建立二維矩陣(如:2 行 4 列的矩陣)
# print(np.random.randn(2,4))

# import numpy as np
# 第一次: 設定種子為 42
# np.random.seed(42)
# print("第一組: ",np.random.randn(3))
# 第二次: 除新設定相同的種子 42
# np.random.seed(42)
# print("第二組: ", np.random.randn(3))
# 第三次: 不設定種子(或換號碼)，結果就會不同
# print("第三組: ",np.random.randn(3))

# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(0)
# x=np.random.randn(100)
# y=np.random.randn(100)
# 可以用遮罩把資料分成兩群，用不同的顏色畫在同一張圖上
# 分成 [x>0] 與 [x<=0]
# mask_pos=x>0
# mask_neg=~mask_pos
# plt.scatter(x[mask_pos],y[mask_pos],c="blue",label="x>0")
# plt.scatter(x[mask_neg],y[mask_neg],c="red",label="x<=0")
# plt.legend()
# plt.title("Masked Scatter")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array(input().split(" "))
# y=np.array(input().split(" "))
# plt.scatter(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(42)
# x=np.random.randn(200)
# y=np.random.randn(200)
# mask_p=x>0
# mask_n=~mask_p
# plt.scatter(x[mask_p],y[mask_p],c="green",label="x>0")
# plt.scatter(x[mask_n],y[mask_n],c="orange",label="x<=0")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(0)
# x=np.arange(50)
# y=x+np.random.randn(50)*5
# plt.scatter(x,y,s=100,alpha=0.6)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as C
r=np.arange(1,11)
a=C.pi*r**2
plt.scatter(r,a)
plt.xlabel("Radius")
plt.ylabel("Area")
plt.title("Circle Area vs Radius")
plt.show()