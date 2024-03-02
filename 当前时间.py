import time

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(now)



import datetime
 
now = datetime.datetime.now()
print(now)

# 格式化日期和时间
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")

# 输出格式化后的日期和时间
print("格式化后的日期：", formatted_date)
print("格式化后的时间：", formatted_time)

