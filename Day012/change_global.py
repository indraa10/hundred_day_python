import constants as c

enemies = 100


def increase_enemies():
    return enemies + 2


def calc():
    return c.pi


def lpg():
    return c.lpg_subsidy


enemy = increase_enemies()
cal = calc()
lp = lpg()

# change the global variable value by using return statement and assign the function to a variable and call it
print(f"number of enemies outside func1: {enemy}")
print(f" imported the module constants , where value of pi : {cal} and value of lpg subsidy : Rs.{lp}/- only")

