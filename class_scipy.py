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

from scipy.optimize import minimize_scalar
def f(x):
    return x**3-3*x   # 有兩個極值點
# 不指定範圍 : 可能找到任意局部最小值
print("無範圍 : ",minimize_scalar(f).x)
# 指定範圍 (0, 3) : 只在此區間找
res = minimize_scalar(f,bounds=(0,3),method="bounded")
print("限制範圍 (0, 3) : ",res.x)
# 指定範圍 (-3, 0)
res = minimize_scalar(f,bounds=(-3,0),method="bounded")
print("限制範圍 (-3, 0) : ",res.x)


