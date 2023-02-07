from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["year","sales"],
                [2001,10001],
                [2002,90000],
                [2003,40002],
                [2004,50040],
                [2005,34572],
                [2006,56775],
                [2007,45672]
    ]

for row in sales_data:
    sheet.append(row)

chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("C://data/linechart.xlsx")