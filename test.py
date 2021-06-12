userinput = int(input("Enter the number: "))

def convert(num):
    num1 = num + userinput
    print(num1)

    for x in range(10):
        num1 += 1
        print(num1)


convert(num=10)