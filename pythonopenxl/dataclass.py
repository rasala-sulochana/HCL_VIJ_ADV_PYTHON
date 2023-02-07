from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class People():
    name:str
    no:int
    age:int#age:int=0
p=[People("sulochana",1,22),People("bujji",2,23),People("Akhila",3,24)]#p=people("sulochana",1)
data=[[p.name,p.no,p.age]for p in p]
data=[["name","no","age"]]+data
for d in data:
    sheet.append(d)
wb.save("C://data/dtcclassdemo.xlsx")
#print(p)