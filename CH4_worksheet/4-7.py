# 計算體脂肪 BMI 值的公式是 W/(H*H)，H 是身高（公尺）和 W 是體重（公斤），請建立 bmil 函式計算 BMI 值，參數是身高和體重。

def bmil(h, w):
    return w / (h ** 2)


h = float(input("請輸入身高（公尺）："))
w = float(input("請輸入體重（公斤）："))

bmi_value = bmil(h, w)
print(f"BMI 值為：{bmi_value:.2f}")