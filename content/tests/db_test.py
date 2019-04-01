
#
#
# test_db.py
#
# Tests for db module
#
#

from ..db import Db


#
# Helpers
#


def start_test_database():

    db = Db(dbname="test_metco")
    return db


#
# Config Tests
#


def test_db_config():
    db = start_test_database()
    db.delete()


#
# Vocab Tests
#


def test_add_vocab():
    db = start_test_database()
    res = db.add_vocab("grade", 5)

    assert res is None

    db.delete()


def test_has_vocab():
    db = start_test_database()
    db.add_vocab("grade", 5)

    res = db.has_vocab("grade", 5)

    assert res is True

    db.delete()


#
#   Translation Tests
#


def test_add_translation():
    db = start_test_database()
    res = db.add_translation("grade", "l", 1)

    assert res is None

    db.delete()


def test_translate():
    db = start_test_database()
    db.add_translation("grade", "l", 1)
    res = db.translate("grade", "l", 1)
    assert res is None

    db.delete()







