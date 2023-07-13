from collections import Counter
d1=Counter('Python')
d2=Counter('HackerEarth')
d=d1&d2

chars = list(d.elements())
chars=sorted(chars)
print(''.join(chars))