import string
import random
x = string.ascii_letters + string.digits+ string.punctuation
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
d = dict()
for ch in z:
    d[ch] = d.get(ch,0)+1

for i in d:
    print(i)