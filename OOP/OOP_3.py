class CellPhone:

    def __inti__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__reteil_price = retail_price

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__reteil_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__reteil_price