from datetime import datetime

def add_timestamp(input_str):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    ms = round(now.microsecond/1000) # ms and us
    # 結合字串和時間
    result_str =  str(current_time) + ":"+ str(ms) + input_str 
    return result_str

f = open("檔案名稱.txt","w")

f.write(add_timestamp("你的資料\n"))
f.write("你很多的資料\n")
f.write("資料很多\n")
f.write("不可思議的多\n")
f.write("超級的多\n")
f.write("終於結束了\n")

f.close()
