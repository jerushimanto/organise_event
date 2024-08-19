import mysql.connector

# Replace with your RDS MySQL endpoint, username, and password
host = "organise-db.cbcelvacwhjp.us-east-1.rds.amazonaws.com"
user = "root"
password = "12345678"

# Establish the connection
connection = mysql.connector.connect(host=host, user=user, password=password,database="aws_organise")

# Create a cursor object to interact with the database
cursor = connection.cursor(dictionary=True)

cursor.execute("select * from events;")
#connection.commit()
a=cursor.fetchall()
for i in a:
    for j in i:print(j)
# Now you're connected and ready to execute SQL queries.
