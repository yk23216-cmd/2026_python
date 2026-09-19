# Pandas
# 專門用來處裡表格型資料的套件，它的資料結構非常像Excel
# 但功能更彈性，也能處裡更大量、更複雜的資料
# 有兩種資料結構Series和DataFrame

# Series 是一維的資料結構，可以想像成是一列資料
# 有index和對應的值，類似 Python 的 list 列表
# 每個值都有對應的索引，而且可以自訂索引名稱

# DataFrame 是二維的資料結構，也就是常說的表格式資料
# 由很多個 Series 組成的一張表格，有列、有欄
# DataFrame 的每一欄都是一個 Series

import pandas as pd

# Pandas 提供自訂的索引(index)
# 列表(list)的索引固定是數字，所以只能用數字來存取資料
# 字典(dict)雖然有 key 可以自訂，但無法向 Pandas一樣快速進行切片、篩選或運算，查詢方式較死板，且缺乏資料表格的結構感
# s1 = pd.Series([90, 80], index=["數學", "英文"])
# print(s1)
# 數學    90
# 英文    80

# Pandas 可以自動對齊不同來源的數據
# 當兩個 Series 或 DataFrame 相加時，Pandas 會根據 index 對齊資料
# 即使兩份資料來源的順序或欄位不一樣，也能正確配對相同的 index
# s2 = pd.Series([85, 70], index=["英文", "數學"])
# print(s1 + s2)
# # 數學    160
# 英文    165

# 使用列表建立Series物件
# score_list = [90, 85, 78, 92, 88]
# name_list = ["小明", "小華", "小蘭", "小函", "小俞"]
# score = pd.Series(score_list, index=name_list)
# print(score)

# 使用字典建立Series物件
# score_dict = {"小明": 90, "小華": 85, "小蘭": 78}
# score = pd.Series(score_dict)
# print(score)

# 指定資料型態
# 32 表示占用 32 個 bit (= 4 bytes)
# 64 表示占用 64 個 bit (= 8 bytes)
# bit 越多，能表示的數字範圍就越大
# score = pd.Series([90, 85, 78], dtype="float64")
# print(score.dtype)
# print(score)

# 使用索引標籤取值
# 如果索引不存在，會KeyError
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score["小美"])


# 使用整數位置取值
# iloc 即為 integer location(整數位置，從0開始數)
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score.iloc[1])  # 85

# 使用條件篩選取值
# Series物件名稱[條件判斷式]
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score[score > 85])
# 為甚麼要這樣設計?
# 首先跟向量化運算有關，一次處裡整個Series，會比用迴圈快很多
# 再來是直覺化操作，條件判斷就像在問問題，答案就是True與False
# 可多個條件篩選，跟numpy一樣
# 且 &
# 或 |
# 非 ~
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score[(score >= 80) & (score <= 90)])

# 切片取值(索引):loc[]
# 前後都包含的閉區間
# loc 全名是 location
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score.loc["小美":"大雄"])  # 最後一個(大雄)是包含的
# 小美    85
# 阿華    78
# 大雄    92

# 切片取值(數字位置):iloc
# iloc[起始位置:結束位置] 結束位置不包含
# 前閉後開的區間
# score = pd.Series([90, 85, 78, 92, 88], index=["小明", "小美", "阿華", "大雄", "小玉"])
# print(score.iloc[1:4])

# 新增值
# fruits = pd.Series([1, 15, 3, 4], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits["芒果"] = 7
# print(fruits)

# 合併:concat()合併多個Series
# fruits = pd.Series([1, 15, 3, 4], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# new_fruits = pd.Series([9, 5], index=["草莓", "西瓜"])
# fruits = pd.concat([fruits, new_fruits])
# print(fruits)

# 修改單一值
# fruits = pd.Series([1, 15, 3, 4], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits["香蕉"] = 3
# print(fruits)

# 修改多個值
# fruits = pd.Series([1, 15, 3, 4], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits[["葡萄", "橘子"]] = [8, 10]
# print(fruits)

# 條件式批次修改
# fruits = pd.Series([1, 15, 3, 4], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits[fruits < 6] = 6 # 把小於6的值全部改成6
# print(fruits)

# 刪除單一值
# fruits = pd.Series([1, 3, 8, 10], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits.drop("草莓", inplace=True, errors="ignore")
# inplace = True 它才會直接修改原 Series
# drop()方法的inplace參數預設是False，就要記得把結果賦值回去
# errors = "ignore" 代表如果指定的索引不存在，Pandas會直接跳過不報錯
# print(fruits)

# 指定索引刪除值
# fruits = pd.Series([1, 3, 8, 10],index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits.drop(["草莓", "鳳梨"], inplace=True, errors="ignore") # 會刪掉鳳梨與對應的值
# print(fruits)


# 條件式刪除
# fruits = pd.Series([1, 3, 8, 10], index=["鳳梨", "香蕉", "葡萄", "橘子"])
# fruits = fruits[fruits < 6]
# print(fruits)
