import mysql.connector
def connect_db():
    # Connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",  # Replace with the correct MySQL server IPv6 address
        user="root",
        password="1807",
        database="community",

    )
    return connection
#
connection = connect_db()
cur = connection.cursor()
cur.execute("SELECT * FROM tbl_user")
rows = cur.fetchall()

for row in rows:
    print(row)
