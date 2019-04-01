#
#
#  parser.py
#
#  Parser Functions
#
#

from config import PARSER_MAPPINGS

#
#  func: based on the desired field, choose the mapped parsing function
#
#  param: field
#  return: parser function if exists or
#


def select_parser(field):

    return PARSER_MAPPINGS.get(field, None)


def city_state_zip(value, field):

    try:
        names = value.split(' ')

        if field == 'student_last':
            return names[0]

        elif field == 'student_first':
            return names[1]

        elif field == 'student_mi':
            if len(names) == 2:
                return ""
            if len(names) == 3:
                return names[2]
        else:
            return False, "{} : {}".format(value, "ERR: Field name not valid for parser")
    except Exception:
        return False, "{} : {}".format(value, "ERR: Couldn't parse city_state_zip into components")


def student_name(value, field):

    try:
        names = value.split(' ')

        if field == 'student_last':
            return names[0]

        elif field == 'student_first':
            return names[1]

        elif field == 'student_mi':
                if len(names) == 2:
                    return ""
                if len(names) == 3:
                    return names[2]
        else:
            return False, "{} : {}".format(value, "ERR: Field name not valid for parser")
    except Exception:
        return False, "{} : {}".format(value, "ERR: Couldn't parse student_name into components")










