from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, likes')

+ likes('Vasya', 'tea')
+ likes('Maria', 'coffee')
+ likes('Vasya', 'coffee')

# Question: who likes coffee
print(likes(X, 'coffee'))