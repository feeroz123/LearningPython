class Student:

    school = "KV"
    city = 'Bangalore'

    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section

    def get_details(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("School = ", self.school)


st1 = Student("Mohan", 10, 'A')

print(st1.school)
print(st1.city)

st1.get_details()
