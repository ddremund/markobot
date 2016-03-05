# markobot naive version

import db
import pymongo

class markobot:

    def __init__(self):
        self.database = db.get_db()

    def create_chain(name, corpus, order):
    
        if database[name].find_one({'_id': "prefs"}):
            return None

    def update_chain(name, corpus, order = 0):

    def persist_chain(chain, name):

    def load_chain(name):

    def update_chain(chain, key, value):

    def join_chains(chain1, chain2):

