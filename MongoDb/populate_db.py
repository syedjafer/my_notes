import pymongo

import uuid

# Replace the following with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017"

# Create a MongoClient object
client = pymongo.MongoClient(mongo_uri)

# Access a specific database (replace 'mydatabase' with your actual database name)
db = client.test

# You can now perform operations on the 'db' object, such as querying or inserting data

# Example: Insert a document into a collection
collection = db.session  # Replace 'my_collection' with your collection name
for num in range(10000000):
    document = {
        "session_id": str(uuid.uuid4()),
        "name": str(uuid.uuid4()),
        "data": []
    }
    collection.insert_one(document)

# Close the connection when done
client.close()
