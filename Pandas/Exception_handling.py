try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
print()

def var(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except TypeError:
        print("Invalid data type Please provide numbers.")
var(15,2)
var(20,0)
var(25,"five")
print()

try:
    a=int(66) 
except ValueError:
    print("Invalid number")
else:
    print("Valid number")
print()

def doo(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print("Division successful")
    finally:
        print("Execution completed.")
doo(16,2)
doo(20,0)
print()

try:
    try:
        a=int("ABC")
    except ValueError:
        print("Invalid Number")
        d=0
    c=100/d
except ZeroDivisionError:
    print("You cannot divide by zero.")
print()