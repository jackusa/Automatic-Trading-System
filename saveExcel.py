 # -*- coding: utf-8 -*-
import sys
import xlwt
import xlrd

from datetime import datetime

reload(sys)                      
sys.setdefaultencoding('utf-8')

class wrExcel():
    def __init__(self):
        self.code = []
        self.date = []

        self.excel = []
        self.sheet = []

        self.initString = ['Name', 'Open', 'CloseYesterday', 'Close', 'Highest', 'Lowest', 'Buy1st', 'Sell1st', 'Volume', 'Amount', 
        'Buy1stVol', 'Buy1st', 'Buy2ndVol', 'Buy2nd', 'Buy3rdVol', 'Buy3rd', 'Buy4thVol', 'Buy4th', 'Buy5thVol', 'Buy5th', 
        'Sell1stVol', 'Sell1st', 'Sell2ndVol', 'Sell2nd', 'Sell3rdVol', 'Sell3rd', 'Sell4thVol', 'Sell4th', 'Sell5thVol', 'Sell5th', 
        'Date', 'Time']

        self.style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')
        self.style1 = xlwt.easyxf('font: name Times New Roman, color-index black') 
        self.style2 = xlwt.easyxf(num_format_str='D-MMM-YY')

    def write(self, code, date, row, data):
        self.code = code
        self.date = date

        self.excel = xlwt.Workbook()
        self.sheet = self.excel.add_sheet(self.code)

        for i in range (len(self.initString)):
            self.sheet.write(0, i, self.initString[i], self.style0)

        

        for i in range (len(data)):
            self.sheet.write(row, i, data[i], self.style1)

        self.excel.save(self.code + '#' + self.date + '.xls')


# excel().write('23423', '23421431', 2, [2342, 37657, 67986, 4545])

#         self.sheet.write(1, 14, datetime.now(), style1)
#         self.sheet.write(2, 15, 1)
#         self.sheet.write(2, 1, 1)
#         self.sheet.write(2, 2, xlwt.Formula("A3+B3"))

# book = xlrd.open_workbook("myfile.xls")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))


