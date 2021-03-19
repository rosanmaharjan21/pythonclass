# class GetterSetter:
#     __name = 'admin'
#
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def get_name(self, new_name):
#         self.__name = new_name
#
#
# obj = GetterSetter()
# obj.get_name = 'hari'
# print(obj.get_name)


class GetterSetter:
    __name = ' '

    def __init__(self):    #this is constructor
        print("I am init method")

    def __new__(cls):
        
    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, new_name):
        self.__name = new_name

    @get_name.deleter  # it deletes the assigned value in property
    def get_name(self):
        del self.__name

    def __del__(self):  # it deletes the object
        print("I am destructor")


obj = GetterSetter()
obj.get_name = 'hari'
print(obj.get_name)
