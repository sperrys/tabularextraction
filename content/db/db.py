
#
#
# db.py
#
# Abstraction for database component
#
#

from pymongo import MongoClient
from config import CONTENT_EXTRACTOR_INPUT_FIELDS, CSV_OUTPUT_FIELDS


class InvalidFieldError(Exception):
    pass


class Db:

    def __init__(self, uri='mongodb://localhost:27017/', dbname='metco', fields=CONTENT_EXTRACTOR_INPUT_FIELDS):

        self.name = dbname

        self.client = MongoClient(uri)
        self.db = self.client[dbname]

        self.fields = fields
        self.translations = self.db['translation']
        self.vocabulary = self.db['vocab']

    #
    #   func: checks whether a field is a valid namespace
    #

    def valid_field(self, field):
        if field not in self.fields:
            raise InvalidFieldError

    #
    #   func: Dumps all the namespaces and values
    #

    def dump(self):
        print("Vocab\n\n")
        self.dump_vocab()
        print("Translations\n\n")
        self.dump_translations()

    def dump_vocab(self):
        for doc in self.vocabulary.find():
            print(doc)

    def dump_translations(self):
        for doc in self.translations.find():
            print(doc)

    #
    #   func: adds a value to the namespace specified by field
    #
    #   params: a valid namespace (must be a valid field), and a value to store
    #   returns: None if new the value is new, if the value exists, return the object id
    #

    def add_vocab(self, field, value):
        self.valid_field(field)
        res = self.vocabulary.update_one({'field': field, 'value': value}, {'$inc': {'count': 1}}, upsert=True)
        return res.upserted_id

    #
    #   func: checks whether a value exists for a given namespace
    #
    #   params: a valid namespace (must be a valid field), and a value to check for
    #   returns: True if the value exists, False if it doesnt.
    #

    def has_vocab(self, field, value):
        self.valid_field(field)
        res = self.vocabulary.find_one({'field': field, 'value': value})
        return res is not None


    #
    #   func: adds a new translation (original word , corrected word ) for a given namespace
    #
    #   params: a valid namespace (must be a valid field), an original value and the translated version
    #   returns: None if the translation didn't exist before and the id of the object if it already existed
    #

    def add_translation(self, field, original, corrected):
        self.valid_field(field)
        res = self.translations.update_one({'field': field, 'original': original, 'corrected': corrected},
                                           {'$inc': {'count': 1}}, upsert=True)
        return res.upserted_id

    #
    #   func: translates (original word -- > corrected word) for a given namespace
    #
    #   params: a valid namespace (must be a valid field), an original word
    #   returns: None if the translation didn't exist before and the id of the object if it already existed
    #

    def translate(self, field, original):
        self.valid_field(field)
        res = self.translations.find_one({'field': field, 'original': original})

        if res is None:
            return None
        else:
            return res['corrected']

    #
    #  func: database deletes itself
    #

    def delete(self):
        self.client.drop_database(self.name)











