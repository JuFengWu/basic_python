try:                      
    a = "123"
    print(a + 1)
except :                   # try內容發生錯誤，就執行 except 裡的內容
    print("error")
print('do something')


try:
    a = 3
    b = 0
    c = a/b
except:
    print("error")
print("do someting 2")
