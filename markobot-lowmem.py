# markbot with minimum memory usage

import db
import pymongo

class markobot:

    def __init__(self, database):
        self.db = db.get_db()

    def create_chain(name, corpus, order):

    def update_chain(name, key, value):