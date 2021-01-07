#how to convert a variable to another type of variable (Casting in Python):
aaa = 123
print(type(aaa))
aaa2 = str(aaa)
print(aaa2)


# flow controll (if - loop - ...)

#for loop
for i in 1, 2, 3, 'start':
    print (i)

#define a fuction
def say_hi_to(n):
    print ('Hi '+n) #do it - on any input

for name in 'ali', 'reza', 'mina', '58', '32':
    say_hi_to(name) #call function

for number in range(1, 10):
    print (number, '-->', number * number)

for u in 'hi', 2, 5, '43', '3333':
    print (u, u*2)

# + in python -> apped - two thing -or- math ex. -> +*/-
# = for a=1
# == for (a=1) == 1