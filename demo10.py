from urllib import parse
wd = "帅哥"
# 中文编码成url中可显示的样式
en = parse.quote(wd)
print(en)
# 解码为中文
print(parse.unquote(en))
# 提取url中的参数
url = "https://www.baidu.com/s?ie=utf-8&wd=ECDEA%W2A%WE%3F%ED"
print(parse.urlsplit(url))