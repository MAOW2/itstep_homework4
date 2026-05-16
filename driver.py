class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    def get_age(self):
        return 2026 - self.birth_year
    def show_info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.get_age())
class Driver(Person):
    def __init__(self, name, birth_year, license_number, driving_experience):
        super().__init__(name, birth_year)
        self.license_number = license_number
        self.driving_experience = driving_experience
    def has_enough_experience(self):
        return self.driving_experience > 2
    def show_info(self):
        super().show_info()
        print("Номер водійського посвідчення:", self.license_number)
        print("Стаж водіння:", self.driving_experience, "років")
        if self.has_enough_experience():
            print("Водій має достатній стаж")
        else:
            print("Водій не має достатнього стажу")
        print()
driver1 = Driver("Олексій", 2000, "AA123456", 5)
driver2 = Driver("Марія", 2005, "BB654321", 1)
driver3 = Driver("Іван", 1998, "CC777888", 3)
driver1.show_info()
driver2.show_info()
driver3.show_info()