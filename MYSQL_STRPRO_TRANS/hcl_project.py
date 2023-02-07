from Hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_seats_avail")
            for r in self.cursor.stored_results():
                seats=r.fetchone()
            return seats

        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Sunayana@447","trainsbooking")
sts=b1.available_seats()
seat_avl={}
seat_avl["train_no"]=sts[0]
seat_avl["train_name"]=sts[1]
seat_avl["Seats_avail"]=sts[2]
print(seat_avl)
