from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, can_marry')


+ can_marry('Ivan', 'Maria')
+ can_marry('Anna', 'Peter')
+ can_marry('Anna', 'John')
+ can_marry('Peter', 'Julia')

# X может жениться на Y, если Y может выйти замуж за X
can_marry(X, Y) <= can_marry(Y, X)

# Вопрос: на ком может жениться Peter
print(can_marry('Peter', X))