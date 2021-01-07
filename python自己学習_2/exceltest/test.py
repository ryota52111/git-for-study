import xlrd
import xlsxwriter

#open old file
old_path = r"C:\Users\r_sas\Desktop\excel_rd.rw\test.xlsx"
old_workbook = xlsxwriter.workbook(old_path)
old_worksheet = old_workbook.add_worksheet()

old_worksheet.write("A1", "list")
old_worksheet.write("A2", "data")

listinput = input(追加したいリストを入力してください)
datainput = input(追加したいデータを入力してください)

lists = []
datas = []
def create_execl(list,data):
    for list in listinput:
        list.append()
        print()


create_execl(listinput,datainput)
