# inner or nested class:a class defined inside class is called inner class or nested class
# Advantages:1.hinding the class 2.reusability

class outer:
    class inner:
        def m1(self):
            print("m1 of method of class inner")
class A:
    class _B:
        def m1(self):
            print("m1 method of inner class")
        def m2(self):
            print("m2 method of inner class")
obj=A._B()
obj.m1()
obj=outer.inner()
obj.m1()
obj=A._B()
obj.m2()


class Person:  # outer class
    class Address:  # inner class
        def __init__(self, s, c):
            self.__street = s
            self.__city = c

        def read_address(self):
            self.__street = input("Enter street: ")
            self.__city = input("Enter city: ")

        def print_address(self):
            print(f"City: {self.__city}")
            print(f"Street: {self.__street}")

    def __init__(self):
        self.__name = None
        self.__address = Person.Address("", "")  # Initialize inner class

    def read_person(self):
        self.__name = input("Enter name: ")
        self.__address.read_address()  # Access inner class method

    def print_person(self):
        print(f"Name: {self.__name}")
        self.__address.print_address()  # Access inner class method


# Corrected instantiation of the Person object
p1 = Person()  # Make sure it's 'Person' (capital P)
p1.read_person()
p1.print_person()
