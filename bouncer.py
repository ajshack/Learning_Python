# ask for age
# age = input("How old are you? ")
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can come in but you can not drink.")
#         # 18 - 21 wristband
#     elif age >= 21:
#         # 21+ drink, normal entry
#         print("You can come in and have drinks!")
#     else:
#         # too young, sorry
#         print("You are too young to enter!")
# else:
#     print("Please enter an age!")


age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 21:
        print("You can come in and have drinks!")
    elif age >= 18:
        print("You can come in but you can not drink.")
    else:
        print("You are too young to enter!")
else:
    print("Please enter an age!")
