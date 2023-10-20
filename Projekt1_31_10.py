import numpy as np
import pandas as pd

space = np.arange(0, 10.1, 0.1)

def G(x, y):
    return 3*x**7 + 2*y**5 - x**3 + y**3 - 3

def G_prim(x, y):
    h = 10e-10
    return (G(x, y) - G(x, y-h))/h

steps = 4
def Newton_method(x, y_k, epsilon):
    global steps
    if abs(G(x, y_k)) < epsilon:
        steps = 4
        return y_k
    else:
        y_k1 = y_k - (G(x, y_k) / G_prim(x, y_k))
        if abs(y_k1 - y_k) < epsilon:
            steps = 4
            return y_k1
        else:
            steps -= 1
            return Newton_method(x, y_k1, epsilon)

def projekt():
    array_ = []
    last_y = 1
    for x in space:
        y = Newton_method(x, last_y, 10e-10)
        last_y = y
        array_.append([x, y, G(x, y)])

    else:
        return np.array(array_)

array = projekt()

dataframe = pd.DataFrame(data=array,
                         index=[i for i in range(len(array))],
                         columns=['x', 'y', 'G(x,y)'])

print(dataframe)
