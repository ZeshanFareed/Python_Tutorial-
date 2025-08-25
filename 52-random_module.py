# jo already pehly se define keay gay ho

# radiant koi bhi no generate kr dega.
# jhan se start hoga woh bhi jahan end hoga woh bhii
import random
r = random.randint(2,5)
print(r)


print()
# radiant koi bhi no generate kr dega but....
# jhan se start hoga woh magr jahan end hoga woh wala no ni dega
r = random.randrange(2,4)
print(r)


print()
# choice koi bhi list tuple wagera se no choice kr k dega
l =[10, 20, 30, 40]
r = random.choice(l)
print(r)



print()
# random float value return krta hy between 0 and 1 k 
s = random.random()
print(s)


print()
# shuffle list mein deay huay kesi bhi no ko shuffle kr sakta hy
l =[10, 20, 30, 40]
random.shuffle(l)
print(l)


print()
# uniform kesi bhi two argument k darmiyan float value deta hy
s = random.uniform(4,6)
print(s)