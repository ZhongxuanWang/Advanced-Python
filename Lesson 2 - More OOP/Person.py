# Illustration of inheritance and polymorphism
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: name-{self.name}, age-{self.age}, gender-{self.gender}"

    def speak(self, words_to_speak):
        print(f"Person \"{self.name}\" spoke: {words_to_speak}")

    @classmethod
    def assign(cls, age):  # This is a factory method
        if age >= 18:
            return Adult(None, None, age)
        else:
            return Child(None, None, age)


class Child(Person):
    def __init__(self, name, gender, age=10, school=None, gpa=None):
        super().__init__(name, age, gender)
        self.school = school
        self.gpa = gpa


class Adult(Person):
    def __init__(self, name, gender, age=18, company=None, spouse=None):
        super().__init__(name, age, gender)
        self.company = company
        self.spouse = spouse


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self, words_to_speak):
        print(f"Dog \"{self.name}\" barked: {words_to_speak}")  # Thou it's not what it's supposed to do..


def makeNoise(obj):
    obj.speak("Hello!")


if __name__ == '__main__':
    a = Person.assign(19)
    b = Child("Child", "Boy", 17, "Stanford", 4.0)
    d = Dog("Puppy")
    makeNoise(a)
    makeNoise(b)
    makeNoise(d)
