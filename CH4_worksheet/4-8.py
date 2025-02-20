# 請建立 Python 程式輸入檔案名稱後，讀取檔案內容來計算共有幾行，程式在讀完後可以顯示檔案的總行數。

import os

file_name = input("Please enter the file name (without extension): ")
file_path = os.path.realpath(file_name + ".txt")
# print(file_path)

if os.path.exists(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(f"The file totals {len(lines)} lines.")
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print("File not found.")
