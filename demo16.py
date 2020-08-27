import csv

# 读取csv
def get_csv():
    with open('./data.csv','r',encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)
# 写入csv
row = [('python','3.7'),('python','3.7'),('python','3.7')]
with open('stock.csv','a+') as f:
    f_writer = csv.writer(f)
    f_writer.writerows(row)
# 以字典形式读取
with open('stock.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)


