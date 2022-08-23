import math


# Numero Uno
for i in range(10+1):
    print(i ** 3)
    if i >1000:
        break

# Numero Dos

for numbs in range(1, 101):
    count= 0
    for i in range (2, (numbs//2+1)):
        if(numbs % i == 0):
            count = count + 1
            break
    if (count == 0 and numbs != 1):
        print(numbs, end= ' ')

# Numero Three!

age = int(input("how old are you?: "))

if age < 18:
    print("kids")
elif age >65:
    print("seniors")
else:
     print("adults")