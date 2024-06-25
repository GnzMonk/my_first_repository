class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_s(self):
        self.__speed = max(self.__speed -5, 0)

    def get_speed(self):
        return self.__speed


def main():
    my_car = Car(2013, "UAZ")
    for _ in range(5):
        my_car.accelerate()
        print(my_car.get_speed())
    for _ in range(8):
        my_car.break_s()
        print(my_car.get_speed())


if __name__ == "__main__":
    main()
