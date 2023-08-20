a = 3
b = 1
c = -1

try:
    if a<0:
        raise
    if b<0:
        raise ValueError("數字要大於0")
    if c <0:
        raise ZeroDivisionError("不能除以0喔~")
except ValueError as msg:
    print(msg)
except ZeroDivisionError as msg:
    print(msg)
except Exception:
    print("有錯誤")
print("continue")
