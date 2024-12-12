import pymysql
def get_connection():
connection = pymysql.connect(
host='172.16.5.126',
user='hotel_user',
password='hoteldb',
db='hotel_reservations',
cursorclass=pymysql.cursors.DictCursor
)
return connection
