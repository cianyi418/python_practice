# 請建立 Python 程式使用串列：［"tom"，"mary"， "joe"］建立成元組，然後建立對應的成績元組，項目是85、76 和 58，在顯示學生數、成績總分和平均後，讓使用者輸入學號來查詢學生姓名和成績。

student_list = tuple(["tom", "mary", "joe"])
score_list = (85, 76, 58)
# student_id = (0, 1, 2)

# students = {
#     student_id[i]: {
#         "name": student_list[i]
#         , "score": score_list[i]} for i in range(len(student_list))
# }
# print(students)

print(f"學生數：{len(student_list)} 成績總分：{sum(score_list)} 平均：{sum(score_list)/len(score_list)}")

while True:
    try:
        student_number = int(input("請輸入學號： ，輸入 -1 結束 "))
        if student_number == -1:
            break
        elif student_number >= 0 and student_number < len(student_list):
            print(f"學生姓名：{student_list[student_number]} 成績：{score_list[student_number]}")
        else:
            print("學號超出範圍")
    except ValueError:
        print("請輸入有效的學號")