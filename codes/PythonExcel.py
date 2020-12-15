import openpyxl
import sys
i = 1
printf = "Pyexcel>>"
while i == 1:
	user = input(printf)
	if user == "new":
		wb = openpyxl.Workbook()
		ws = wb.active
		print("创建工作表成功!")
		printf = printf + str(ws.title) + ">"
	if user[0] == "t" and user[1] == "i" and user[2] == "t" and user [3] == "l" and user[4] == "e":
		titler = user.split(" ")
		ws.title = titler[1]
		print("修改名称成功!")
		printf = "Pyexcel>>" + str(ws.title) + ">"
	if user[0] == "s" and user[1] == "e" and user[2] == "t":
		seter = user.split(" ")
		ws[seter[1]] = seter[2]
		print(f"成功:已经把{seter[1]}的内容填充为{seter[2]}.")
	if user == "save":
		wb.save("wb.xlsx")
		print(f'已经保存为{sys.argv[0]}\\wb.xlsx')
