# 使用 with open
# r 读取文件
# w 创建文件，会覆盖源文件
# a 追加文件，不存在会创建
# b 操作二进制流
# a+ rw的集合
# 写入
with open('test.txt','a+') as f:
    f.write('python')
# 读取
with open('test.txt','r') as f:
    content = f.readlines()
    for c in content:
        print(c.strip())

