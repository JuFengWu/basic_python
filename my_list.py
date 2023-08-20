x = []

y = [1,2,3,4]

z = [1,"aa",2,"bb"]

print(y)
print(z)

y.append(5)

print(y)


y.pop()
print(y)

del y[0:3] # [0,3]表示0~2，不包含3
print(y)


print(z[1]) #取出第一個元素?

z[1] = 8
print(z)


valueList = [1,2,3,4,5]

print(valueList[0:3])
print(valueList[:2])
print(valueList[1:])
print(valueList[:])
