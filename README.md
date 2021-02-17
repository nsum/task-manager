### Requirements.txt
- in order for flask to communicate to mongo we need to install flask-pymongo (similar to pymongo)
- in order to use mongo connection string we need to install dnspython
- after adding any libs or packages always update requirements.txt so app knows what to use

### Indexing and Searching
- start interpreter with python3
- from app import mongo : this is the var mongo that we created on top of app.py and used throughout project
- mongo.db.tasks.create_index([("task_name", "text"), ("task_description", "text")])
    - we can only have one index at one time
- mongo.db.tasks.index_information() : shows information
- 