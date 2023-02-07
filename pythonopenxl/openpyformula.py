import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook("C://data/demoformula.xlsx")
sheet=wb.active
sheet["A7"]="=SUM(A1:A6)"
wb.save("C://data/newsheet.xlsx")