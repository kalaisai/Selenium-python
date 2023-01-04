import openpyxl
path="C:\\Users\\KalaimathiSaiKannan\\Documents\\newxl.xlsx"
book = openpyxl.load_workbook(path)
sheet = book.active


for i in range(8, 6):
    for j in range(5, 8):
        sheet.cell(row=i, column=j).value = "kalai"

book.save(path)

