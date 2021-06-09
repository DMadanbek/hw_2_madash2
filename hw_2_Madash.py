class Person:
    __total_persons = 0
    __year=2021
    def __init__(self,name,birth_year,**kwargs):
        if self.__year > 2021:
            raise Exception("Ошибка")
        self.__name=name
        self.__birth_year=birth_year
        self.__language=kwargs.get('language')
        Person.__total_persons+=1


    def get_language(self):
        return self.__language

    def is_adult(self):
        return 2021-self.__birth_year >=18

    def get_age(self):
        return self.__year-self.__birth_year

    @classmethod
    def get_total_persons(cls):
        return cls.__total_persons

    def talk(self):
        print("Hello World")

class Teacher(Person):
    def talk(self):
        print(f"Greetings, I'm your teacher {self.__name}")

    def teach(self,name):
        print(f"Lesson started by {self.__name}")
#
p1 = Person('Nurdin', 12,language='kyrgyz')
p2 = Person('Jakie Chan', 22, language='chinese')
p3 = Person('Chingachkuk', 25, language=' korean')
t1 = Teacher('Romeo', 22, language='spanish')
t2 = Teacher('John', 20, language='english')
t3 = Teacher('Putin', 25, language='russian')



print(Person.get_total_persons())
