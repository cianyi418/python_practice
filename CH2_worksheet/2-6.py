# 請建立 Python 程式使用多選一條件敘述檢查動物園的門票，120 公分下免費，120~150 半價，150 以上為全票？

height = int(input("enter height: "))

if height < 120:
    print("Take a ticket for free!")
elif 120 <= height < 150:
    print("Half price for a ticket!")
else:
    print("Full price for a ticket!")