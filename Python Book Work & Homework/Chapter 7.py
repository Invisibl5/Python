import sys
#1 Basic Moon Weight Function
def moon_weight(weight,increase):
    x=1
    y=weight
    z=increase
    while x<=15:
        print(increase)
        print(weight)
        weight=weight*.165
        print("you will weigh",weight,"kilos on the moon")
        weight=y+increase
        increase=increase+z
        x=x+1
moon_weight(50, .5)

#2 Moon Wieght Function And Years
def moon_weightyears(weight,increase,years):
    x=1
    y=weight
    z=increase
    while x<=years:
        print(increase)
        print(weight)
        weight=weight*.165
        print("you will weigh",weight,"kilos on the moon")
        weight=y+increase
        increase=increase+z
        x=x+1
moon_weightyears(50, .5, 10)

#3 Moon Weight Program
def moon_weightyearssys():
    print("what is your earth weight?")
    weight=int(sys.stdin.readline())
    print("how much weight will you gain?")
    increase=int(sys.stdin.readline())
    print("how many years?")
    years=int(sys.stdin.readline())
    x=1
    y=weight
    z=increase
    while x<=years:
        print("increase is", increase)
        print("earth weight is", weight)
        print("it is year", x)
        weight=weight*.165
        print("you will weigh",weight,"kilos on the moon")
        weight=y+increase
        increase=increase+z
        x=x+1
moon_weightyearssys()