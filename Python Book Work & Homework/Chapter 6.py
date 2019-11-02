#1 The Hello Loop: answer: says hello 0
for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
#2 Even Numbers
x=1
while x<=13:
    print(x)
    x=x+23
#3 My five favorite Ingredients
ingredients=["tomato","lettuce","patty","ketchup","cheese"]
x=1
c=0
while x<6:
    print(x,ingredients[c])
    x=x+1
    c=c+1
#4 Your Weight On The Moon
weight=100
x=1
while x<+15:
    weight=weight*.165
    print("you will weigh",weight,"kilos on the moon")
    weight=100+x
    x=x+1