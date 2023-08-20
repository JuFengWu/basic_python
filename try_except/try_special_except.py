try:
    #print(3/0)
    a=3
    c = a/b
except ZeroDivisionError:
    # 捕捉除以零的例外
    print("不能除以零!")
except Exception:
    print("總之有個錯誤")

print("do something")   
