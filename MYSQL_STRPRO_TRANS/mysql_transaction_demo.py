from mysql.connector import Error
from Hcl_database_connection import MysqlDatabaseConnection
class Hclpythontransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        cust_id = 2
        sql = "delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(cust_id,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj=Hclpythontransaction()
connect_obj.connect("localhost","root","Sunayana@447","hcl_vijayawada")
connect_obj.execute_transaction_query()