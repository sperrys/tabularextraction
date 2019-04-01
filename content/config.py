
#
#
#   Config.py
#
#   Configuration options for content extractor and validator
#


DATA_PATH = 'data/'
OUTPUT_PATH = 'output'


#
#  Input fields from the structural extraction phase
#

CONTENT_EXTRACTOR_INPUT_FIELDS = ["student_name", "community_name", "school_name", "grade", "school_name", "grade",
                                  "birth_date", "guardian_name", "home_address", "city_state_zip", "family_num",
                                  "emergency_contact", "emergency_phone", "mother_employ_phone", "father_employ_phone",
                                  "status", "home_phone"]


#
#  Relative Structural Positioning of input fields, (row, col) format
#


RELATIVE_RECORD_INPUT_FIELD_GRID = { 'student_name': (0, 0), 'community_name': (0, 1), 'school_name': (0, 2),
                                     'grade': (0, 3), 'birth_date': (0, 4), 'guardian_name': (1, 0),
                                     "home_address": (1, 1), "city_state_zip": (1, 2), 'family_num': (1, 4),
                                     'emergency_contact': (2, 0), "emergency_phone": (2, 1), "mother_phone":(2, 2),
                                     "father_phone": (2, 3), "status": (2, 4), 'home_phone': (3, 0)}

#
#  Desired fields of csv output
#


CSV_OUTPUT_FIELDS = ["student_first", "student_last", "student_mi","community_name", "school_name", "grade",
                     "birth_date", "guardian_name", "home_address", "city", "state", "zip_code", "family_num",
                     "emergency_contact", "emergency_phone", "mother_employ_phone", "father_employ_phone",
                     "status", "home_phone"]


PARSER_MAPPINGS = {'student_first': 'student_name', 'student_last': 'student_name', 'student_mi': 'student_name',
                   'city': 'city_state_zip', 'state': 'city_state_zip', 'zip_code': 'city_state_zip'}


INPUT_PDF = 114
PAGE_END = 385
INTERVENE = False


