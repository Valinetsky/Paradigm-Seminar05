from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, frends, is_frends')


+ frends('Ivan', 'Maria')
+ frends('Anna', 'Peter')
+ frends('Anna', 'John')
+ frends('Peter', 'Julia')

# X может жениться на Y, если Y может выйти замуж за X
is_frends(X, Y) <= frends(X, Y) or frends(Y, X)

# Вопрос: на ком может жениться Peter
print(is_frends('Anna', X))