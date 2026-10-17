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

import numpy as np
from scipy.interpolate import interp1d
x=np.array([0,1,2,3])
y=np.array([1,3,7,13])
fl=interp1d(x,y,kind="linear")
squ=lambda x:x*x
n_x=np.array([0.5,1.5,2.5])
n_y=squ(fl(n_x))
print("Sum of Squares: %.2f"%(np.sum(n_y)))