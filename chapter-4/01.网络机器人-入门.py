import requests
from lxml import html


#定义url
target_url = "https://www.tiobe.com/tiobe-index/"

#发送请求，获取数据
response = requests.get(target_url)

#输出数据到控制台
# print(response.text)
doc = html.fromstring(response.text)

#解析数据
#解析表头
# list_th = doc.xpath("//table[@id='top20']/thead/tr/th/text()")

# full xpath
# list_th = doc.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()")

# xpath
list_th = doc.xpath("//*[@id='top20']/thead/tr/th/text()")
print(list_th)
# 解析数据
list_tr = doc.xpath("//table[@id='top20']/tbody/tr")
for tr in list_tr:
    list_td = tr.xpath("./td/text()")
    print(list_td)

# HTML:负责网页结构（内容）
# CSS:负责网页样式（页面美化）
# JS:负责网页交互（行为）
