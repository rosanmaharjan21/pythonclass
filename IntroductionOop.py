class IntroductionOop:
    def __init__(self):  # this is constructor and it is auto callable and self is introductionOop
        print("python")

    x = 10

    def test(self):
        print(self.x)


obj = IntroductionOop()
print(obj.test())
# print(dir(obj))


# for calculator

# class IntroductionOop:
#     def __int__(self):
#         p=int(input("Enter p: "))
#         t = int(input("Enter t: "))
#         r = int(input("Enter r: "))
#         return