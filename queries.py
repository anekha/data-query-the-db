# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

def query_orders(db):
    # return a list of orders displaying each column
    query = """SELECT *
            FROM Orders
            ORDER BY OrderID
            """
    db.execute(query)
    results = db.fetchall()
    #results_list = []
    #for result in results:
        #results_list.append(result[])
    return results

def get_orders_range(db, date_from, date_to):
    t = (date_from, date_to)
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = """SELECT *
            FROM Orders
            WHERE OrderDate > ?
            AND OrderDate <= ?
            """
    db.execute(query, t)
    results = db.fetchall()
    return results

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = """ SELECT *, (JULIANDAY(ShippedDate) - JULIANDAY(OrderDate)) as TimeDelta
            FROM Orders
            ORDER BY TimeDelta
            """
    db.execute(query)
    results = db.fetchall()
    return results


print(query_orders(db))
print(get_orders_range(db, '2012-04-28', '2012-12-14'))
print(get_waiting_time(db))
