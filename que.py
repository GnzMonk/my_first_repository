class Que:
    def __init__(self, elem):
        self.__res_list = []
        self.__res_list.append(elem)

    def add(self, elem):
        self.__res_list.append(elem)

    def get(self):
        last_elem = self.__res_list[0]
        del self.__res_list[0]
        return last_elem

    def __str__(self):
        return f"{self.__res_list}"

my_que = Que(1)
my_que.add(2)
print(my_que)
print(my_que.get())
print(my_que)