# # def total_number(*number):
# #     size_of_array = len(number)
# #     x = 0
# #     sum = 0
# #
# #     while x < size_of_array:
# #         sum += number[x]
# #         x += 1
# #
# #     print(sum)
# #
# #
# # total_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
#
# def total_number(*number):
#     size_of_array = len(number)
#     x = 0
#     sum = 0
#     even_total = 0
#     odd_total = 0
#     while x < size_of_array:
#         if number[x] % 2 == 0:
#             even_total += number[x]
#         else:
#             odd_total += number[x]
#         sum += number[x]
#         x += 1
#
#     print(f"Total number: {sum}")
#     print(f"Total even: {even_total}")
#     print(f"total odd: {odd_total}")
#
#
# total_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def si(p,t,r):
    return (p*t*r)/100
    p=int("Enter value for p")
    t=int("enter value for t")
    r=int("enter r")

print(si(10,10,10))