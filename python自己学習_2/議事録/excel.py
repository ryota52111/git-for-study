import xlsxwriter


outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

names = ["Kyle","Bob","Mary"]
values = [70,82,71]

outSheet.write("A1", "Names")
outSheet.write("B1", "Scores")


for item in range(len(names)):
    outSheet.write(item+1, 0 ,names[item])
    outSheet.write(item+1, 1 ,values[item])

outSheet.write("D1", "Total") 
outSheet.write_formula("D2", "=SUM(B2:B4)")

# outSheet.write(1, 0, names[0])
# outSheet.write("A3", names[1])
# outSheet.write("A4", names[2])

# outSheet.write("B2", names[0])
# outSheet.write("B3", names[1])
# outSheet.write("B4", names[2])



outWorkbook.close()