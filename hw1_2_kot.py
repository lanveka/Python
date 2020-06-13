# алгоритм решения ребуса КОТ + КОТ = ТОК
k = int()
o = int()
t = int()
p = int()
p = 0
for k in range(1,10):
    for o in range(0,10):
        for t in range(1,10):
           if (200*k+20*o+2*t == 100*t+10*o+k)and(k!=o)and(k!=t)and(o!=t):
               print([str(k)+str(o) +str(t) + "+" + str(k) +str(t)+str(o) + "=" + str(t)+str(o)+str(k)])
               p += 1
if p==0:
    print("решений нет")

