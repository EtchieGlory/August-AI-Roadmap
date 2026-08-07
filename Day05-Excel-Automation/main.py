from openpyxl import Workbook


workbook = Workbook()
sheet = workbook.active
sheet.title = "Students"

sheet["A1"] = "Name"
sheet["B1"] = "Score"

sheet["A2"] = "John"
sheet["B2"] = 85

sheet["A3"] = "Mary"
sheet["B3"] = 92

sheet["C1"] = "Grade"
sheet["C2"] = "A"

workbook.save("output/students.xlsx")

print("Excel file created sucessfully")