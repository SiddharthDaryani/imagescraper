import pymongo
import urllib.parse
username= urllib.parse.quote('siddharthdaryani')
password= urllib.parse.quote('sidd@SQL567')
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@siddharth.ipwvs0o.mongodb.net/?retryWrites=true&w=majority")
data= {"key":"value", 'name':'mahesh'}
db = client['trial']
review_col = db['yn']
review_col.insert_one(data)