a = 1
def func():
    global a
    a = 5



func()
print(a)

class Student:
    student_count = 0

    def __init__(self, id, name):
        self.name = name
        self.id = id
        Student.student_count += 1

    def show_count(self):
        print("Total number of students", Student.student_count)

    def show_info(self):
        print("ID: ", self.id, "Name: ", self.name)

if __name__ == "__main__":

    tripto = Student("1205001", "Nafis Irtiza")
    sadat = Student("1905001", "Sadat Hossain")

    # print(tripto.name, tripto.id)
    # print(sadat.id, sadat.name)

    tripto.show_info()

    # del tripto.name
    # sadat.show_info()
    # tripto.show_info()

    del Student.student_count


    print(Student.student_count)

    # __del__(obj)