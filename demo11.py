import re
text = '<a href="www.baidu.com">'\
    'python</a>'

r = re.compile('<a href="(.*?)"',re.I|re.S)


# result = re.match('<a href="(.*?)"',text,re.I|re.S)
# print(result)
# print(result.group())
# print(result.groups())  # 必须加上括号
result = r.findall(text)
print(result)