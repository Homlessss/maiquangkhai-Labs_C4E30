import pymongo

client = pymongo.MongoClient("mongodb+srv://homlessss:4BQoyCkal5qV7r6r@cluster0-yzgzn.mongodb.net/test?retryWrites=true")
db = client.test

def get_all():
    return list(db.xedaps.find({}))

def add_xedap(model,daily_fee,image_url,year):
    db.xedaps.insert_one({'Model' : model, 'Daily_fee' : daily_fee, 'Image_url' : image_url, 'Year' : year})
