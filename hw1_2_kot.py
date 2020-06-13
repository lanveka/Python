k = int()
o = int()
t = int()
p = int()
a = int()
b = int()
p = 0
for k in range(1,10):
    for o in range(0,10):
        for t in range(1,9):
           if (200*k+20*o+2*t == 100*t+10*o+k)and(k!=o)and(k!=t)and(o!=t):
               print((k,o,t,'+',k,o,t,'=',t,o,k))
               p += 1
           else:
               print("решений нет")

