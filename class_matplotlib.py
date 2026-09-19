# 散佈圖(scatter)
# import matplotlib.pyplot as plt  # 引入函式庫並重新命名
#
# x = [1, 2, 4, 6, 8, 1, 2, 9, 3]  # 準備資料
# y = [5, 7, 2, 3, 1, 4, 6, 5, 8]
# plt.title("Simple Plot")  # 設定圖名
# plt.xlabel("x")  # 設定X軸名稱
# plt.ylabel("y")  # 設定Y軸名稱
# plt.scatter(x, y, c="r")  # 繪製散佈圖
# plt.savefig("散佈圖.png", dpi=300) # 可以儲存圖表，要寫在plt.show()前，dpi是圖片解析度
# plt.show()  # 呈現所繪圖表

# 垂直長條圖(bar)
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 7, 8, 6, 9]
# plt.bar(x, y, color="r")
# plt.show()

# 水平長條圖(barh)
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 7, 8, 6, 9]
# plt.barh(x, y, color="r")
# plt.show()

# 折線圖(plot)
# import matplotlib.pyplot as plt

# plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 設定字型為微軟正黑體
# x = [1, 2, 3, 4, 5]
# y = [2, 7, 8, 6, 9]
# plt.xlabel("X軸")
# plt.ylabel("Y軸")
# plt.plot(x, y, "o", color="r")  # 繪製折線圖(只有點)
# plt.show()

# plt.xlabel("X軸")
# plt.ylabel("Y軸")
# plt.plot(x, y, color="r")  # 繪製折線圖(只有線(預設))
# plt.show()

# plt.xlabel("X軸")
# plt.ylabel("Y軸")
# plt.plot(x, y, "-o", color="r")  # 繪製折線圖(點和線)
# plt.show()

# plt.xlabel("X軸")
# plt.ylabel("Y軸")
# plt.plot(x, y, "--o", color="r")  # 繪製折線圖(點和虛線)
# plt.show()

# 範例
# apple = []
# banana = []
# import matplotlib.pyplot as plt
# import csv

# f = open("fruit_data.csv", "r", encoding="utf-8-sig")
# for row in csv.DictReader(f):
#     if row["Year"] == "2017":
#         apple.append(int((row["Apple Price"])))
# f.close()
# f = open("fruit_data.csv", "r", encoding="utf-8-sig")
# for row in csv.DictReader(f):
#     if row["Year"] == "2017":
#         banana.append(int((row["Banana Price"])))
# f.close()
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# y = apple
# Y = banana
# plt.xlabel("month")
# plt.ylabel("price")
# plt.title("apple vs banana")
# plt.plot(x, y, "-o", color="r")
# plt.plot(x, Y, "-o", color="b")
# plt.savefig("apple vs banana", dpi=300)
# plt.show()
