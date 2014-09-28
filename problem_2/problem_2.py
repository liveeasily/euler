'''
Fn = 0 , if n = 0;
or 1, if n = 1;
or Fn-1 + Fn-2, if n > 1

F0 = 0
F1 = 1,  odd
F2 = 1,  odd
F3 = 2,  even (odd+odd)
F4 = 3,  odd (odd+even)
F5 = 5,  odd (odd+even)
F6 = 6,  even (odd+odd)
...

So, if n is mutiples of 3, Fn is even.
'''


sum  = 0
fibo_seq = [0, 1]
index = 2
while 1:
    fibo_seq.append(fibo_seq[index-2] + fibo_seq[index-1])
    if fibo_seq[index] >= 4000000:
        print sum
        break
    if index % 3 == 0:
        sum += fibo_seq[index]
    index += 1


