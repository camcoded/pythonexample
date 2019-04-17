L1=[1,10,0,5]

try:
    L=int(input("Enter the location"))
    no1=int(input("Enter any number"))
    no2=int(input("Enter any number"))
    result=(L1[L]+no1)/no2
    print("The result is",result)
except ZeroDivisionError:
    print("Do not divide any number by zero")
except ValueError:
    print("only use numbers")
except IndexError:
    print("list index out of range")
