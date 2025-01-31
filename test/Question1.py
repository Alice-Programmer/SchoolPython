import random

Man=[0]
Sen=[0]

for i in range(1,11,1):
    r=random.randrange(1,11)
    if r<=3:
        Man.append(Man[i-1]+0)
        Sen.append(Sen[i-1]+6)
    else:
        Man.append(Man[i-1]+1)
        Sen.append(Sen[i-1]+0)

print(Man)
print(Sen)