# named tuples

# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
#
# users = (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com')
#
# # user = User(users[0], users[1], users[2], users[3], users[4])
#
# user = User(*users)
#
# print(user.name, user.lastname)


# ------------------------------------------------------


# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
# users = [
#     (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (2, 'Sobir', 'Toxirov', 18, 'Sobir@gmail.com'),
#     (3, 'Toxir', 'Sobirov', 35, 'Jalil@gmail.com'),
# ]
#
# for user in users:
#     employee = User(*user)
#     print(employee.id, employee.name, employee.lastname, employee.email)


# ------------------------------------------------------
#
# from collections import namedtuple
#
# User = namedtuple('User', 'id name lastname age email')
#
# users = [
#     (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (2, 'Sobir', 'Toxirov', 18, 'Sobir@gmail.com'),
#     (3, 'Toxir', 'Sobirov', 35, 'Jalil@gmail.com'),
# ]
#
# for user in users:
#     us = User(*user)
#     print(us.id, us.name, us.lastname, us.age, us.email)
#
#
# car = ('Malibu', 'Red', '300 km/h', 20000, 4, 'Avtomat')

