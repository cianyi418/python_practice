# 請寫出 Python 程式執行從 1 到 100 的迴圈，但只顯示 40 ~ 67 之間的奇數，並且計算總和。

i = 1
total_sum = 0

while i <= 100:
    if i >= 40 and i <= 67 and i % 2 != 0:
        print(i)
        total_sum += i
    i += 1

print(f"Total = {total_sum}")