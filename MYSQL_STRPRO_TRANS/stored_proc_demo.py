from mysql.connector import Error
from Hcl_database_connection import MysqlDatabaseConnection
class HclstoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata=("puri",)
            self.cursor.callproc("get_cust_dtls",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj=HclstoredProcedure()
connect_obj.connect("localhost","root","Sunayana@447","hcl_vijayawada")
print(connect_obj)
connect_obj.execute_str_procedure()