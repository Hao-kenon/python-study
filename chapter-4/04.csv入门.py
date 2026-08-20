#csv 操作 - 方式一:文件操作的原始方式
# 写
# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("name,age,sex,hobby\n")
#     f.write("小王,18,男,'football,running'\n")
#     f.write("小张,19,女,swimming\n")
#     f.write("小李,20,男,basketball\n")


# 读

# with open("csv_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())



#csv 操作 - 方式二:csv(推荐)
import csv

# 写
# with open("csv_data/02.csv","w",encoding="utf-8",newline="") as f:
#     writer = csv.DictWriter(f,fieldnames=["name","age","sex","hobby"])
#     writer.writeheader() #写入表头 fieldnames
#     writer.writerow({"name":"小王","age":18,"sex":"男","hobby":"football,running"})
#     writer.writerow({"name":"小张","age":19,"sex":"女","hobby":"swimming"})
#     writer.writerow({"name":"小李","age":20,"sex":"男","hobby":"basketball"})
#
# 读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
