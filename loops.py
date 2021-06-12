# userinput = int(input("Enter the number: "))

# def convert(num):
#     num1 = num + userinput
#     print(num1)

#     for x in range(10):
#         num1 += 1
#         print(num1)


# convert(num=10)


letter = ['w','r','t','o','l','h','c','v']

letter1 = ['f','b','x','n','r','w','t']

letter2 = ['f','b','x','o','l','h','c']

combined_list = letter+letter1+letter2

user_input = input("Enter the Char:\n")

if user_input in combined_list:
    print("You guess right")
else:
    print("You guess wrong")


