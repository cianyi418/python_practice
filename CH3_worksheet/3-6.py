#  請在 Python 程式建立一個空串列，在輸入4筆學生成績資料：95、85、76、56 和新增至串列後，計算成績的總分和平均。

score_list = []

print("請輸入學生成績，輸入完成請輸入 '*' 結束")
while True:
    score = input("請輸入學生成績： ")
    if score == '*':
        break
    else:
        score_list.append(int(score))

print(f"Total score: {sum(score_list)} Average score: {sum(score_list)/len(score_list)}")
