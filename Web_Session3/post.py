import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.c4e

db.posts.insert_one({
    'title' : 'c4e30',
    'author' : 'Mai Quang Khải',
    'content' : 'Mình sinh năm 1999 nha bạn Khánh. ĐỪng gọi mình là a, Please. Nghe già vc :v'
})

