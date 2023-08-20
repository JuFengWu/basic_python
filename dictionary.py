

data = {"國文":89,"英文":65,"數學" : 80}

print(data)

data["國文"] = 88

print(data)

data["程式"] = 100

print(data)

del data["國文"]

print(data)

for x in data:
    print(x)

for key,value in data.items():
    print(key,value)

    



