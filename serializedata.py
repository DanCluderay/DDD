import pickle
import json
from phpserialize import serialize, unserialize


df='a:2:{i:0;a:2:{s:3:"qty";i:1;s:5:"price";s:4:"0.39";}i:1;a:2:{s:3:"qty";i:3;s:5:"price";s:4:"0.33";}}'
data=serialize("wow")
b = bytes(df, 'utf-8')
data=unserialize(b)

print(data)