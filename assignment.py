# assignment num 1 to login
# userName: "admin"
# password: "admin002"
#
# userName = str(input("Enter the userName: "))
# password = str(input("Enter the password: "))
# if userName == "admin" and password == "admin002":
#     print("welcome")
# else:
#     print("Enter the valid username and password")

# # assignment num 2 to find simple interest
# principle = int(input("Enter the principle amount: "))
# time = int(input("Enter the time: "))
# rate = int(input("Enter the rate: "))
# SI = (principle * time * rate) / 100
#
# print("The Simple Interest is ", SI)


# assignment no 3 preparing markSheet
studentName = str(input("Enter the name of student: "))
print("The name of student is", studentName)
englishMarks = int(input("Enter the marks scored in English: "))
if englishMarks>100:
    print("Please enter marks between 0-100")
mathMarks = int(input("Enter the marks scored in Math: "))
scienceMarks = int(input("Enter the marks scored in Science: "))
nepaliMarks = int(input("Enter the marks scored in Nepali: "))
socialMarks = int(input("Enter the marks scored in Social: "))
totalMarks = englishMarks + mathMarks + scienceMarks + nepaliMarks + socialMarks
percentage = (totalMarks / 500) * 100
print("The total marks you scored is: ", totalMarks)
print("The percentage you scored is: ", percentage)
if englishMarks < 35 or mathMarks < 35 or scienceMarks < 35 or nepaliMarks < 35 or socialMarks < 35:
    print("You are fail")
else:
    print("You are pass")

if percentage < 45:
    print("Third")

elif percentage < 60:
    print("second")

elif percentage < 75:
    print('first')
else:
    print("top")

if englishMarks < 35:
    print("Your are fail in english")