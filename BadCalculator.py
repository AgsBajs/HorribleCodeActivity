#Global Variables For No Reason At All - Keep it simple keep it stupid Violation
g1 = None
g2 = None
inpt = ""
cache =  [] #Storing our answers but will never use them - YAGNI Violation

#Useless

def func1(a,b):
    print("Adding now...")
    return a + b

def func2(a,b):
    print("Subtracting now...")
    return a - b

def func3(a,b):
    print("Multiplying now...")
    return a * b

def func4(a,b):
    print("Dividing now...")
    return a / b

print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("q.Quit")

while True:
    op = input()  # no prompt; unclear UX
    if op == "q":
        print("bye")
        break

    if op not in ("1", "2", "3", "4"):
        print("Invalid Input")
        # keep going anyway (don’t continue), so we’ll still ask for numbers - Complex and Unneeded
    try:
        g1 = float(input("Enter first number: "))   # globals mutated for no reason
    except:
        print("bad number, using 0")  # bare except
        g1 = 0
    try:
        g2 = float(input("Enter second number: "))
    except:
        print("bad number, using 0")
        g2 = 0

    # duplicate branching instead of a simple map
    if op == "1":
        res = func1(g1, g2)
        print(g1, "+", g2, "=", res)
        cache.append(res)  # stored input but never used
    elif op == "2":
        res = func2(g1, g2)
        print(g1, "-", g2, "=", res)
        cache.append(res)
    elif op == "3":
        res = func3(g1, g2)
        print(g1, "*", g2, "=", res)
        cache.append(res)
    elif op == "4":
        res = func4(g1, g2)
        print(g1, "/", g2, "=", res)
        cache.append(res)
    else:
        # fallthrough path prints something anyway - Complex and Confused
        print("Doing addition by default")
        res = func1(g1, g2)
        print(g1, "+", g2, "=", res)

    # repeat the menu inline instead of reusing the function - DRY violation
    print("Select Operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("q.Quit")