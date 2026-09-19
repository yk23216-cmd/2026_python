# 為甚麼使用Numpy
# Python列表處理速度很慢
# Numpy提供比列表快50倍的陣列
# 陣列在數據科學中使用非常頻繁，速度和資源很重要

# Numpy vs Python 列表差異
#
# 1.資料類型
# - Numpy 陣列:所有元素必須是相同資料型態 節省記憶體、存取更快
# - Python 列表:可以存放不同資料型態 彈性大但效率低
# 2.執行基礎
# - Numpy:底層用C語言實作 接近硬體速度快
# - 列表:用Python撰寫 效率相對較慢
# 3.記憶體儲存方式
# - Numpy:使用連續記憶體空間 存取快
# - 列表:用指標指向分散的記憶體 存取慢
# 4.運算方式
# - Numpy:支援向量化運算 可直接對整個陣列做加減乘除
# - 列表:需要用迴圈逐一處理元素

# 範例
# import numpy as np  # 習慣上用np當縮寫
#
# print(np.array([1, 2, 3]) + np.array([5, 6, 7])) # [ 6  8 10]
# print([1, 2, 3] + [5, 6, 7])  # [1, 2, 3, 5, 6, 7]

# 陣列
# 有順序且連續性方式儲存資料
# 陣列裡的資料都稱為元素(Element)
# 每個元素都有索引
# 元素的資料型態都一致
# (n)維陣列會以(n-1)維陣列為元素

# 從Python列表建立numpy陣列
# import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# print(a)  # [1 2 3 4 5]

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print("形狀 shape:", b.shape) # 形狀 shape: (2, 3)
# print("維度 ndim:", b.ndim) # 維度 ndim: 2
# print("元素型態 dtype:", b.dtype) # 元素型態 dtype: int64
# 快速建立陣列
# print(np.zeros(2, 3))  # 建立 2X3 全部為 0 的陣列
# print(np.ones(3, 3))  # 建立 3X3 全部為 1 的陣列
# print(np.arange(0, 10, 2))  # [0 2 4 6 8] # 使用參數方法同range
# print(np.linspace(0, 1, 5))  # [0. 0.25 0.5 0.75 1.]
# np.linspace()產生等差數列的方法

# Numpy不需要寫for迴圈就可以簡單做運算
# x=np.array([1,2,3])
# y=np.array([10,20,30])
# print(x+y)  # [11 22 33]
# print(x*y)  # [10 40 90]
# print(x**2) # [1 4 9]
# print(x+10) # [11 12 13]

# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = arr.reshape(2, 3)  # (row, column)
# print(newarr)
# [[1 2 3]
#  [4 5 6]]
# 記得轉換前後的元素個數要相同否則會出現錯誤

# 陣列篩選
# scores = np.array([55, 80, 72, 90, 45, 60])
# # 篩選出 >= 60分的人
# passed = scores[scores >= 60]
# print(passed) # [80 72 90 60]

# 多條件篩選
# 篩選60~80分的學生
# & and
# | or
# ~ not
# Python:and or not 處理單一值
# numpy:& | ~ 處理整個陣列
# scores = np.array([55, 80, 72, 90, 45, 60])
# mid = scores[(scores >= 60) & (scores <= 80)]
# print(mid)  # [80 72 60]

# 陣列布林索引
# scores = np.array([55, 80, 72, 90, 45, 60])
# print(scores >= 60) # [False  True  True  True False  True]
# print(scores[scores >= 60]) # [80 72 90 60]

# scores = np.array([55, 80, 72, 90, 45, 60])
# 1.基本統計
# print("總和 sum:", np.sum(scores))  # 總和 sum: 402
# print("平均 mean:", np.mean(scores))  # 平均 mean: 67.0
# print("中位數 median:", np.median(scores))  # 中位數 median: 66.0
# print("標準差 std:", np.std(scores))  # 標準差 std: 15.275252316519467
# print("變異數 var:", np.var(scores))  # 變異數 var: 233.33333333333334
# # 2.最大/最小
# print("最高分 max:", np.max(scores)) # 最高分 max: 90
# print("最低分 min:", np.min(scores)) # 最低分 min: 45
# # 3.其他常用數學函數
# print("每個分數的平方:", np.square(scores)) # 每個分數的平方: [3025 6400 5184 8100 2025 3600]
# print("每個分數開根號:", np.sqrt(scores)) # 每個分數開根號: [7.41619849 8.94427191 8.48528137 9.48683298 6.70820393 7.74596669]
# print("每個分數的log(自然對數):", np.log(scores)) # 每個分數的log(自然對數): [4.00733319 4.38202663 4.27666612 4.49980967 3.80666249 4.09434456]

# 一維陣列取值
# 和 Python 列表類似，使用索引
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])  # 10
# print(arr[2])  # 30
# print(arr[-1])  # 取最後一個元素 50

# 二維陣列取值
# # 格式:arr[列, 行]
# mat = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(mat[0, 0])  # 1
# print(mat[1, 2])  # 6
# print(mat[2, -1])  # 9

# 切片
# 和Python列表一樣，但可以同時對 列 和 行 取範圍
# print(arr[1:4])      # [20 30 40]
# print(mat[0:2, 1:3]) # [[2 3]
#                      #  [5 6]]
# print(mat[:, 0])     # [1 4 7]
# print(mat[1, :])     # [4 5 6]

# numpy 修改元素

# import numpy as np

# mat = np.array([1, 2, 3])
# mat[0] = 10
# print(mat)  # [10  2  3]


