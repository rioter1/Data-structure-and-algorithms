import functools
@functools.lru_cache()
def fib(n):
    if n<4:
        return n
    return fib(n-1)+fib(n-2)

print(fib(10))

from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare the data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape to a column vector
y = np.array([2, 4, 5, 4, 5])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(x, y)

# Extract the model parameters
slope = model.coef_[0]
print(slope)


t={}
t[(11,2,49)]=18
t[(49,10,21)]=7
t[(15,19)] = 20
s=0
for i in t:
    s+=t[i]
print(s**len(t))