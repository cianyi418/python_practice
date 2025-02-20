# 請在 Python 程式建立 get max() 函式傳入 3 個參數，可以回傳參數中的最大值；get_sum() 和 get_average() 函式共有 4 個參數，可以計算參數成績資料的總分與平均值。

def get_max(a,b,c):
    return max(a,b,c)

def get_sum(a,b,c,d):
    return sum([a,b,c,d])

def get_average(a,b,c,d):
    total = get_sum(a,b,c,d)
    return total/4


print(get_max(1,2,3))
print(get_sum(1,2,3,4))
print(get_average(1,2,3,4))


