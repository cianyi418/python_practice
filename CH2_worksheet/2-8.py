# 請建立 Python 程式輸入繩索長度，例如：100 後，使用 while 迴圈計算繩索需要對折幾次才會小於 20 公分？

rope_length = int(input("Enter the length of the rope: "))
fold_times = 0

while rope_length >= 20:
    rope_length /= 2
    fold_times += 1

print(f"The rope needs to be folded {fold_times} times to be less than 20 cm.")