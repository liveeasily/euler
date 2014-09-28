'''
sum = 0
for multiple3 in range (3, 1000, 3):
    sum += multiple3

for multiple5 in range (5, 1000, 5):
    sum += multiple5

for multiple15 in range (15, 1000, 15):
    sum -= multiple15
print sum
'''

'''
sum = 0
for n in range(3, 1000):
    if (n%3) == 0 or (n%5) ==0:
        sum += n
print sum
'''

'''
print sum([n for n in range(3, 1000) if n%3 == 0 or n%5 == 0])
'''

print sum([n for n in range(3, 1000, 3)])\
      + sum([n for n in range(5, 1000, 5)])\
      - sum([n for n in range(15, 1000, 15)])

