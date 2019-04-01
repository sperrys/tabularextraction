
#
#  Record.py
#


class Record(object):

    def __init__(self, book_number="", page_number="", school_year="", student_first="", student_last="", student_mi="", community_name="",
                 school_name="", grade="", birth_date="", guardian_name="", home_address="", city="", state="",
                 zip_code="", family_num="", emergency_contact="", emergency_phone="", mother_employ_phone="",
                 father_employ_phone="", status="", home_phone="", app_date="", address_label_code=""):

        self.book_number = book_number
        self.page_number = page_number
        self.school_year = school_year
        self.student_first = student_first
        self.student_last = student_last
        self.student_mi = student_mi

        self.community_name = community_name
        self.school_name = school_name
        self.grade = grade
        self.birth_date = birth_date
        self.guardian_name = guardian_name

        self.home_address = home_address
        self.city = city
        self.state = state
        self.zip_code = zip_code

        self.family_num = family_num
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self.mother_employ_phone = mother_employ_phone
        self.father_employ_phone = father_employ_phone
        self.status = status
        self.home_phone = home_phone
        self.app_date = app_date
        self.address_label_code = address_label_code


    def dict(self):

        return {
            "book_number": self.book_number,
            "page_number": self.page_number,
            "school_year": self.school_year,
            "student_first": self.student_first,
            "student_last": self.student_last,
            "student_mi": self.student_mi,
            "community_name": self.community_name,
            "school_name": self.school_name,
            "grade": self.grade,
            "birth_date": self.birth_date,
            "guardian_name": self.guardian_name,
            "home_address": self.home_address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "family_num": self.family_num,
            "emergency_contact": self.emergency_contact,
            "emergency_phone": self.emergency_phone,
            "mother_employ_phone":  self.mother_employ_phone,
            "father_employ_phone":  self.father_employ_phone,
            "status": self.status,
            "home_phone": self.home_phone,
            "app_date": self.app_date,
            "address_label_code": self.address_label_code
        }
