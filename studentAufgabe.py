class Student:
    def __init__(self, name, matnr):
        self.__name = name
        self.__matnr = matnr
        self.__modules = {}

    def add_module(self, modnr, grade):
        self.__modules[modnr] = grade

    def get_avggrade(self):
        sum = 0
        for mod in self.__modules:
            sum += self.__modules[mod]
        return sum / len(self.__modules)       

    def print_gradingtable(self):
        print("Courses : ","Grade: ") ,
        for i in self.__modules:
            print(str(i)+": "+ str(self.__modules[i])+" ")
        print(str("Average Grade:"+str(self.get_avggrade())))
stud1 = Student("Joreg", 121)

stud1.add_module("T121", 4.1)
stud1.add_module("T103", 4.0)
stud1.add_module("A111", 4.0)

print(stud1.print_gradingtable())