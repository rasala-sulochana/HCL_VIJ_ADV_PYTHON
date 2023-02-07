import pandas as pd
import numpy as np
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        return self.df
    def total_df(self):
        self.df['total']=self.df.iloc[:,2:].sum(axis=1)
        return self.df
    def avg_df(self):
        self.df["avg"]=self.df["total"]/5
        return self.df
    def rank_df(self):
        self.df["Rank"] = df["avg"].rank()
        return self.df
    def result_df(self):
        df["Result"] = np.where(
            (df["Python"] >= 35) & (df["Mysql"] >= 35) & (df["C"] >= 35) & (df["C++"] >= 35) & (df["Java"] >= 35),
            "Pass", "Fail")
        return self.df

obj=Readcsv()
df=pd.read_csv("C://data/student.csv")

# print(obj.create_df(df))
# print(obj.total_df())
# print(obj.avg_df())
# print(obj.rank_df())
# print(obj.result_df())
# print(obj.(create,total,avg,rank,result)_df())
# print(df)







# df=pd.read_csv("C://data/student.csv")
# df["Total"]=df.iloc[:,2:].sum(axis=1)
# df["avg"]=df["Total"]/5
# d=""
# df["Rank"]=df["avg"].rank()
# #print(df)
# df["Result"]=np.where((df["Python"]>=35) & (df["Mysql"]>=35) & (df["C"]>=35) & (df["C++"]>=35) & (df["Java"]>=35),"Pass","Fail")
# print(df.sort_values(by=["Rank"]))