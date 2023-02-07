import pandas as pd
import os
exldata1=pd.read_excel("C://Users/user796/Documents/Book01.xlsx",sheet_name="Sheet1")
print(exldata1)
exldata2=pd.read_excel("C://Users/user796/Documents/Book01.xlsx",sheet_name="Sheet2")
print(exldata2)
#exldata1.to_html
#exdata3=pd.concat([exldata1,exldata2],axis=1,join="inner")
#exdata4=pd.merge(left=exldata1,right=exldata2,how="inner")
# print(exldata1.compare(exldata2))
exldata3=pd.concat([exldata1,exldata2])
print(exldata3)
