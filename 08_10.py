input_number = 10
count = 0
for number in range(2, input_number):
    if input_number % number == 0:
        print("bakhsh paziri bar -> ", number)
        #print(number,)
        count += 1

if count == 0:
    print("addad avval ast")

#brak - continue - optimaize