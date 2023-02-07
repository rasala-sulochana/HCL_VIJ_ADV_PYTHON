from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook=load_workbook(filename="C://data/hcllogo.xlsx")
sheet=workbook.active
logo=Image("C://data/hcl.JFIF")
logo.height =150
logo.width=150
sheet.add_image(logo,"E5")
workbook.save(filename="C://data/hcl.xlsx")

