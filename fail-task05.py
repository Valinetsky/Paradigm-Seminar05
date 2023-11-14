from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, age, total_age, number_of_people')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

# Определение общего возраста
# total_age = sum_([d[1] for d in age])
#total_age(X) <= sum_(Y, for_each=age(X, Y))
# total_age = sum_([d[1] for d in age])

total_age[X] = sum_(age[X], for_each=Y)
average_age = total_age[X] / len_(X)
print(average_age)


# len_ (P[X]==len_(Y)) <= body : P[X] is the count of values of Y (associated to X by the body of the clause)


# # Определение количества людей
number_of_people(Z) <= len_(X, age(X, Y))

# # Расчет среднего возраста
# average_age(Y) <= (total_age(X) and number_of_people(Z)) and (Y == X/Z)

# # Запрос среднего возраста
# print(average_age(Y))



# from pyDatalog import pyDatalog
# pyDatalog.create_terms('X, Y, age, total_age')

# age('Мария', 30)
# age('Иван', 40)
# age('Алексей', 20)

# total_age[X] = sum_(age[X], for_each=Y)
# average_age = total_age[X] / len_(Y)

# print(average_age)