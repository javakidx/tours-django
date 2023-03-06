import certifi
from django.http import JsonResponse
from pymongo import MongoClient

mongodb_connection_string = 'mongodb+srv://app-dev:qRCycvCC4mQrvjSQ@cluster0.deys8ga.mongodb.net/?retryWrites=true&w=majority'


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host, port=int(port), username=username, password=password)
    db_handle = client[db_name]

    return db_handle, client


def get_db():
    client = MongoClient(mongodb_connection_string, tlsCAFile=certifi.where())
    return client['natours']


def get_tour_collection():
    return get_db().tours


def get_not_found_response(message):
    return JsonResponse({'code': 'not_found', 'message': message}, status=404)
