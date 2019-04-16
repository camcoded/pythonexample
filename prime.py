number = int(input("Enter any number: "))


if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("is not a prime number")
            break
    else:
        print("is a prime number")

else:
    print("is not a prime number")
