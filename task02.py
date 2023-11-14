from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, parent, grandparent')

# Отношения родительства
+ parent('Maria', 'Ivan')
+ parent('Ivan', 'John')

# Определение отношения "дедушка/бабушка"
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)

# Question: who is granny and grandpa for John
print(grandparent(X, 'John'))