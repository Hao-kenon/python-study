import re

s1 = "18000000001,phone_number1;phone_number2:18000000002"
s2 = "phone_number1:18000000001;phone_number2:18000000002"
#match
result = re.match(r"1[3-9]\d{9}", s1)
print(result.group())#获取匹配到的结果
print(result.span())#匹配项的索引
print(result.start())#开始索引
print(result.end())#结束索引


#search
result = re.search(r"1[3-9]\d{9}",s2)
print(result.group())#获取匹配到的结果
print(result.span())#匹配项的索引
print(result.start())#开始索引
print(result.end())#结束索引

#findall
result = re.findall(r"1[3-9]\d{9}",s1)
print(result)