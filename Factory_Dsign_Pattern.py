# @Creation Date :  27/12/2022
# Description:      when we want to decide at run time which object to create, separation of concerns, mind your own business kind of pattern
#increase the modularity

from abc import ABCMeta, abstractstaticmethod
# we have an abstract p[erson class (interface), we don't ewant to decide in the code whether we would like to create
# a teacher object or student object dynamically during the run time
class IPerson(metaclass=ABCMeta): # good notation for saying something is interface, meta is used for saying we can not create instances, abstract class
    @abstractstaticmethod
    def person_method():
        """"interface method- just a signature of the method, not the actual definition"""

#p1=IPerson()


class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")

# s1=Student()
# t1=Teacher()
# s1.person_method()
# t1.person_method()

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()

        if person_type == "teacher":
            return Teacher()

        print("invalid type")
        return -1

if __name__=="__main__":
    choice= input("What type of person do you want to create?\n")
    person=PersonFactory.build_person(choice)
    person.person_method()
