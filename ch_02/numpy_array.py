from ast import Index
import numpy as np
import pandas as pd

data = np.genfromtxt(
    'example_data.csv', delimiter=';', 
    names=True, dtype=None, encoding='UTF'
)

#print(data)

array_dict = {}
for i, col in enumerate(data.dtype.names):
    array_dict[col] = np.array([row[i] for row in data])
#print(array_dict['time'])

x = np.array([value[array_dict['mag'].argmax()] for key, value in array_dict.items()])
#print(x)

place = pd.Series(array_dict['place'], name = 'place')
#print(place)

place_index = place.index
#print(place_index.is_unique)

#print(np.array([1,1,1]) + np.array([-1,0,1]))
s1 = pd.Series(np.linspace(0,10, num=5))
s2 = pd.Series(np.linspace(0,10,num=5), Index([1,2,3,4,5]))
#print(s1+s2)

df = pd.DataFrame(array_dict)
print(df + df)
