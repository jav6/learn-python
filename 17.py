# use pylint in ide for check syntax

tel={} #-> dic
#tel[] -> list

tel={'hadi':'+98-0054', 'saeed':'00254'}
tel['mahdi1']='+1-0025'
#tel={'mahdi2':'+1-0025'}

print(tel)

del tel['mahdi1']

print(tel)

print(tel['saeed'])

#tel.get() for set empty
#tel.key() for show key and value
#x in tel if isset x -> true

for a in tel.items():
    print(a)

#tuple in python
mytuple = (1, "a", "b", "c")