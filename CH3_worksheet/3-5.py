# 請在 Python 程式建立 10 個項目的串列，串列項目值是索引值 +1，然後計算項目值的總和與平均。

list = []

for _ in range(10):
    item = int(input("請輸入串列項目："))
    list.append(item)

print(f"串列項目值：{list}")
print(f"串列項目值總和：{sum(list)} 串列項目值平均：{sum(list)/len(list)}")