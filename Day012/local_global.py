enemies = 1

enemies2 = 10

enemies3 = 100


def increase_enemies():
    enemies = 2
    return print(f"number of enemies in func1: {enemies}")


# here calling the function will invoke the variable mentioned within the function
increase_enemies()
# here calling the variable directly will invoke the global variable
print(f"number of enemies outside func1: {enemies}")


# both the variables are different and to make the two same name variable as same we need to use global keyword .

def increase_enemies2():
    global enemies2  # with this code global variable came under local function
    enemies2 = 20  # modified the global variable
    return print(f"number of enemies in func2: {enemies2}")


increase_enemies2()

print(f"number of enemies outside func2: {enemies2}")


# Thumb rule : Don't Try to modify the global variable within local scope
# instead use return statement

def increase_enemies3():
    print(f"number of enemies in func3: {enemies3}")
    return enemies3 + 2


increase_enemies3()

print(f"number of enemies outside func3: {enemies3}")
