class Empty:

    """An empty class without constructor."""

    pass



class Person:

    """Represent a person with firstname, lastname, and age."""


    def __init__(self):

        """Initialize a new Person instance with optional parameters."""

        self.firstname = ""

        self.lastname = ""

        self.age = 0
        
    pass


class Student:

    """Represent a student with firstname, lastname, and age."""


    def __init__(self, firstname=None, lastname=None, age=None):

        """Initialize a new Student instance with optional parameters."""

        self.firstname = firstname

        self.lastname = lastname

        self.age = age


    def __str__(self):

        """Return a string representation of the Student."""

        return f"{self.firstname} {self.lastname}, Age: {self.age}"



if __name__ == '__main__':

    # Empty class usage

    empty_instance = Empty()

    print("Created an instance of Empty class:", empty_instance)


    # Creating 3 Person instances

    person1 = Person("John", "Doe", 30)

    person2 = Person("Jane", "Smith", 25)

    person3 = Person("Alice", "Johnson", 28)


    print("\nPersons:")

    print(person1)

    print(person2)

    print(person3)


    # Creating 3 Student instances

    student1 = Student("Tom", "Brown", 20)

    student2 = Student("Lucy", "Green", 22)

    student3 = Student("Mark", "White", 19)


    print("\nStudents:")

    print(student1)

    print(student2)

    print(student3)