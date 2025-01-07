# Course Class

class Course:

    def __init__(self, code, name, units, category):
        self._code = code
        self._name = name
        self._units = int(units)
        self._category = category
        self._level = None
        self._faculty = None
        self._school = None
        self._prereqs = None

    def __str__(self):
        return f"{self._code}: {self._name} \n{self._units} units \n{self._category}"

    def print_full(self):
        print(f"{self._code}: {self._name} \n{self._units} units \n{self._category}")
        print(self._level)
        print(self._faculty)
        print(self._school)
        print("Prerequisites: " + str(self._prereqs))

    def get_code(self):
        return self._code
    def get_name(self):
        return self._name
    def get_units(self):
        return self._units
    def get_category(self):
        return self._category
    def get_level(self):
        return self._level
    def get_faculty(self):
        return self._faculty
    def get_school(self):
        return self._school
    def get_prereqs(self):
        return self._prereqs
    def set_details(self, level, faculty, school, prereqs):
        self._level = level
        self._faculty = faculty
        self._school = school
        self._prereqs = prereqs
