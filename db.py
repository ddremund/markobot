# Markobot MongoDB singleton

from pymongo import MongoClient

_connection = None
_db = None

def get_conn():
    global _connection
    if not _connection:
        _connection = MongoClient("localhost", 27017)
    return _connection
    
def get_db():
    global _db
    if not _db:
        _db = get_conn().markobot
    return _db
    
__all__ = ["get_conn","get_db"]