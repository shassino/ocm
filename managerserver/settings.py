import json
import pymysql
#import configuration
with open('settings.json') as f:
    config = json.load(f)

db = pymysql.connect(host=config['DB_HOST'], user=config['DB_USER'], passwd=config['DB_PASSWORD'], db=config['DB_NAME'])
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)
