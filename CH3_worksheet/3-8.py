# 請改用字典建立學習評量7. 的Python 程式，姓名是鍵；成績是值。

student_list = tuple(["tom", "mary", "joe"])
score_list = (85, 76, 58)

students = dict(zip(student_list, score_list))

print(students)


while True:
    name = input("請輸入學生姓名來查詢成績，輸入 -1 結束： ")
    if name == "-1":
        break
    elif name in students:
        print(f"學生姓名：{name} 成績：{students[name]}")
    else:
        print("查無此人")