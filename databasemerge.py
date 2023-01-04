import random

purchase = []
with open('Database.txt') as p:
    for line in p:
        purchase.append(line.strip())
    
stylee = []
with open('Style.txt') as p:
    for line in p:
        stylee.append(line.strip())

color = ['Denim', 'Cotton', 'Leather', 'Satin', 'Polyester', 'Linen']

for i in range (len(purchase)):
    with open('FINAL.txt', 'a') as p:
        p.write(purchase[i] +" " + stylee[i])
        p.write('\n')

'''
r = random.SystemRandom()
for i in range(90):
    with open('FINAL.txt', 'a') as p:
            p.write(str(r.randint(0,0)))
            p.write('\n')
'''          




