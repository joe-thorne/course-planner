# Course Class

class Course:

    def __init__(self, code, name, units, category):
        self._code = code
        self._name = name
        self._units = int(units)
        self._category = category

    def __str__(self):
        return f"{self._code}: {self._name} \n{self._units} units \n{self._category}"

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_units(self):
        return self._units
    
    def get_category(self):
        return self._category
