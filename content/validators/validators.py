#
#
#  validators.py
#
#


import datetime


def student_mi(value):
    return string(value, length=1)


def student_first(value):
    return string(value)


def student_last(value):
    return string(value)


def community_name(value):
    return string(value)


def grade(value):
    return number(value, min=1, max=12)


def birth_date(value, format="%d/%m/%Y"):

    try:
        datetime.datetime.strptime(value, format)
        return True, value
    except Exception:
        return False, "{} : {}".format(value, "ERR: Not a valid birth date")


def guardian_name(value):
    return string(value)


def home_address(value):
    return string(value)


def city(value):
    return string(value)


def state(value):
    return string(value, length=2)


def zip_code(value):
    return number(value, num_digits=5)


def family_num(value):
    nums = value.strip('/')
    if len(nums) != 2:
        return False, {"{} : {}".format(value, "Not a valid family number!")}


def mother_employ_phone(value):
    value.replace("-", "")
    return number(value, num_digits=10)


def father_employ_phone(value):
    value.replace("-", "")
    return number(value, num_digits=10)


def status(value):
    known_status = ['active']

    if value not in known_status:
        return False,


########################
#                      #
#    Base Validators   #
#                      #
########################


#
#  func: validates a number with different options
#
#  params:
#       needed:   string value
#       optional: number of digits to have in value, min value, max value
#
#  return:
#       False if any options isn't validated, and error message
#


def number(value, num_digits=None, min=None, max=None):

    # Catch All if for no if clause gets hit

    res = False, "{} : {}".format(value, "ERR: number wasn't validated at all: {}".format(max))

    if not value.isdigit():
        return False, "{} : {}".format(value, "ERR: Not a valid Number")

    # number of digits options

    if num_digits is not None and len(value) != num_digits:
        return False, "{} : {}".format(value, "ERR: Not the right number of digits: ")

    # min and max permutations

    if min is not None:
        if min < int(value) > max:
            return False, "{} : {}".format(value, "ERR: Number not between min: {} and max: {} inclusive!".format(min, max))
    if max is not None:
        if max < int(value):
            return False, "{} : {}".format(value, "ERR: Number not equal or above max: {}".format(max))

    return res, value


#
#  func: validates a string with different options
#
#  params:
#       needed:   string value
#       optional: number of digits to have in value, min value, max value
#
#  return:
#       False if any options isn't validated, and error message
#


def string(value, length=None):

    # base check
    try:
        for c in value:
            if c.isdigit():
                return False, "{} : {}".format(value, "ERR: Not a valid string ")

        # length check

        if length is not None and len(value) != length:
            return False, "{} : {}".format(value, "ERR: String not the right length: Should be length {}".format(length))
        return True, value

    except Exception:
        return False, "{} : {}".format(value, "ERR: Not a valid string ")




