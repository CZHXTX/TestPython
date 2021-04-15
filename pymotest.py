import pymongo

#链接数据库
client = pymongo.MongoClient('mongodb://wnms:wnmswnmswnmswnms@47.93.6.250:27017/admin')
db = client.WNMS_CSNew2020
collection = db.Sws_DeviceJKInfo

#查询一条数据
print('单条数据','='*50)
result = collection.find()
print(result)
