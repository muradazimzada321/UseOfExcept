check = True
while check:
 try:
    n1 = int(input("Number 1 "))
    n2 = int(input("Number 2 "))
    print(r"Pick up an operation to be processed on ",n1," and ",n2)
    operation = input("+ or - or * or / :")
    if operation == "+":
     print(n1, " + ", n2, " = ", n1 + n2)
    elif operation == "-":
     print(n1, " - ", n2, " = ", n1 - n2)
    elif operation == "*":
     print(n1,  " * ", n2, " = ", n1 * n2)
    elif operation == "/":
     print(n1, " / ", n2, " = ", n1 / n2)

    check = False

 except ValueError:
    print("Only operation can be processed on numbers...\n"
          "Please enter only numbers ")
    print("Enter values again")
 except ZeroDivisionError:
    print("Can not divide zero")
    print("Enter values again")
