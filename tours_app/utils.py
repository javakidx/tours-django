from pymongo import MongoClient
import certifi

mongodb_connection_string = ''


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host, port=int(port), username=username, password=password)
    db_handle = client[db_name]

    return db_handle, client


def get_db():
    client = MongoClient(mongodb_connection_string, tlsCAFile=certifi.where())
    return client['natours']
