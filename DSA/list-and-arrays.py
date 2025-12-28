#looking for the second to the largest number
x = [2, 4, 1, 7, 5, 35]

y = x[0]
print(y)

for n in x:
    if n > y:
        y = n

print(y) 