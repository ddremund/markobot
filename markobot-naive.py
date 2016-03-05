# markobot naive version

import db
import pymongo

class markobot:

    def __init__(self, name):
        self.database = db.get_conn()[name]

    def create_chain(self, name, corpus, order):
    
        if self.database.find_one({'_id': name}):
            return None
        self.database.update({'_id': name}, {'$set': {'__ORDER__': order}})


    def update_chain(self, name, corpus, order = 0):

    def persist_chain(self, chain, name):

    def load_chain(self, name):

    	return self.database.find_one({'_id': name})

    def update_chain(self, chain, key, value):

    def join_chains(self, chain1, chain2):

    def dict_from_corpus(self, corpus, order):

    	with open(filename) as corpus:
    		words = corpus.read()
    		i = iter(words.split())
    		tokens = map(" ".join,zip(*[i]*order))
    	
    	tokens.append("")
    	token_map = dict.fromkeys(tokens, [])

    	prev_token = ""

    	for token in tokens:
    		token_map[last_token].append(token)
    		last_token = token

    	return token_map



