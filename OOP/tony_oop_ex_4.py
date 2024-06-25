class Employee:
    def __init__(self, name, id, office, post):
        self.__name = name
        self.__id = id
        self.__office = office
        self.__post = post

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_office(self):
        return self.__office

    def get_post(self):
        return self.__post

    def __str__(self):
        return f"{self.__name} {self.__id} {self.__office} {self.__post}"

def main():
    emp1 = Employee("Сьюзан Мейерс", "47899", "Бкхгалтерия", "Вице-презтдент")
    print(emp1)

if __name__ == "__main__":
    main()