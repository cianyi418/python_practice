# 目前網路商店正在週年慶折扣，消費1000元，就有 8 折的折扣，請建立 Python 程式輸入消費額為 900、2500 和 3300 時的付款金額？

def cal_coast(coast):
    if coast >= 1000:
        coast *= 0.8
    return int(coast)

test_payment = [900, 2500, 3300]
for payment in test_payment:
    print(f"消費金額為: {payment}，付款金額: {cal_coast(payment)} 元")