class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.id)

    def do_thing(self):
        pass


# Simple example class usage (client code)
def run_demo():
    s = Student()
    print(s)
    s.do_thing()

    # first_name = input("First name: ")
    # last_name = input("Last name: ")
    # student_id = int(input("ID: "))
    # s1 = Student(first_name, last_name, student_id)
    # print(s1.first_name, "has ID", s1.id)


if __name__ == '__main__':
    run_demo()
