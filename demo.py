# # # # # *array arguments = tuple
# # # # # ** keywords =  dictionary
# # # #
# # # # def names(*name, **nm):
# # # #     print(name)
# # # #     print(nm)
# # # #
# # # #
# # # # # names('ram', 'sita', 'gita', name='hari', age=20)
# # #
# # # x = 10
# # #
# # #
# # # def test():
# # #     global x
# # #     print(x)
# # #     x = x + 3
# # #     print(x)
# # #
# # #
# # # test()
# #
# #
# # def test():
# #     x = 10
# #     return x
# #
# #
# # print(test())
# # a = test()
# # print(a)
#
# def test():
#     def get():
#         return "hello get"
#
#     return get
#
#
# # print(itan()) gives the location
# print(test()())

def get_name():
    num_of_student = int(input("Enter number of students: "))
    students = []
    x = 0
    while x < num_of_student:
        name = input("Enter name: ")
        students.append(name)
        x += 1

    return students


def display():
    for name in get_name():
        get_name()


display()


def display():
    pass
