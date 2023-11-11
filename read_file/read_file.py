file1 = open("檔案名稱.txt", "r")

content = file1.read()  # 讀取整個檔案的內容
print("完整內容：")
print(content)
file1.seek(0)  # 將檔案讀取指標歸零，準備重新讀取檔案
a = file1.read(8)  # 讀取一行內容
print(a)
file1.seek(0)  # 將檔案讀取指標歸

line_num =0
while True:
    line = file1.readline()
    if not line:
        break
    print(line.strip())# 去除行尾換行符號
    line_num += 1
