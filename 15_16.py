#for use a function(on py) - ex. : random() -> use import random
#for import a library in python and set name for it - import matplotlib.pyplot as plot
#-------------------------------------------------------------------------------------
import random

random.seed()

people = []
# test > 50 -replace-> range(0,50)
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 100):
    for person1 in range(0, 50):
        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)

        if people[person1] != 0:
            # print(person1, person2)
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1

#print(people)

#GUI
import matplotlib.pyplot as plt

#%matplotlib inline #for show in notebook
# people.sort()
plt.bar(range(0, 50), sorted(people, reverse=True))