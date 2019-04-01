
#
#
#   main.py
#
#

import os
import csv
import pandas as pd

from db import db
from record import record
from validators import validators
from parsers import parsers
from viewer import viewer

from config import INPUT_PDF, DATA_PATH, CSV_OUTPUT_FIELDS, PAGE_END, INTERVENE, \
     RELATIVE_RECORD_INPUT_FIELD_GRID, OUTPUT_PATH


db = db.Db()
viewer = viewer.Viewer()


#
#   Consume a value based on its CSV_OUTPUT_FIELDS field
#


def consume_field(page, field):

    r, c = RELATIVE_RECORD_INPUT_FIELD_GRID['field']

    value = viewer.get_cell(page, r, c)

    # If the vocab says the value exists, or we have a translation already for the value.
    has_word = db.has_word(field, value)
    translation = db.translate(field, value)

    if has_word is False:
        return value
    elif translation is not None:
        return translation
    # If not see if we can try to naively validate the field
    else:

        # First, see if we need to parse the field
        #
        # If a parser exists, it means an output field is embedded as one of many
        # within an input field. So we must reduce to the right value before validation.
        # This selection is done with config.PARSER_MAPPINGS

        parser = parsers.select_parser(field)

        if parser is not None:
            value = parser(value, field)

        # attempt to validate the desired out
        is_valid, result = validate_field(field, value)

        # if our validators say it's valid, add to vocab and write
        if is_valid:
            db.add_vocab(field, value)
        else:
            return False, result


#
#   Validate a value based on its CSV_OUTPUT_FIELDS field
#


def validate_field(field, value):

    func = getattr(validators, field)
    is_valid, result = func(value)

    if not is_valid:
        return False, "{} : {}".format(value, "ERR: Validation: {}".format(field, value))


#
#   Consume Page
#


def consume_page(writer, page):

    file = os.path.join(DATA_PATH, str(INPUT_PDF) + "_page_1_" + ".csv")
    f = pd.read_csv(file, header=None)
    viewer.add_view(f, page)
    consume_records(writer, page)


#
#  Consume all records on a page
#


def consume_records(writer, page):

    r = record.Record()

    while viewer.current_page() == page:

        for field in CSV_OUTPUT_FIELDS:

            valid, value = consume_field(page, field)

            if valid:
                setattr(r, field, value)
            else:
                setattr(r, field, value)

        writer.writerow(r.dict())



#
#  Main Driver
#


if __name__ == '__main__':

    output_file = os.path.join(OUTPUT_PATH, str(INPUT_PDF) + ".csv")

    with open(output_file, mode='w+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_OUTPUT_FIELDS)

        for page in [p + 1 for p in range(PAGE_END)]:
            consume_page(writer, page)


