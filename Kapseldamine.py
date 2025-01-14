class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__status = "Active"

    def get_id(self):

        return self.__student_id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_status(self, status):
        valid_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        if status in valid_statuses:
            self.__status = status

    def get_status(self):
        return self.__status
