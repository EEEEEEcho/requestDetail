import xlwt
import xlrd
def create():
    Excel_book = xlwt.Workbook()
    sheet1 = Excel_book.add_sheet("1")
    sheet1.write(0,0,'python')
    Excel_book.save('test.xls')

create()

def get_data():
    data = xlrd.open_workbook("test.xls")
    # 获取第一个sheet
    sheet = data.sheets()[0]
    # 获取行数和列数
    nrows = sheet.nrows
    ncols = sheet.ncols
    # 获取行数据
    for i in range(nrows):
        print(sheet.row_values(i))
    # 获取列数据
    for j in range(ncols):
        print(sheet.col_values(j))
get_data()