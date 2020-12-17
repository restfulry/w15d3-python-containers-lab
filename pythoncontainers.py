# Exercise 1
print('- Exercise 1 -')
students = ['Bob', 'Joe', 'Billy', 'Sally', 'Kim']

print(f"Second Student: {students[1]}")
print(f"Last Student: {students[-1]}")

# Exercise 2
print('- Exercise 2 -')
foods = ('sushi', 'ice cream', 'chocolate', 'steak', 'spaghetti')

for food in foods:
    print(f"{food} is a good food.")

# Exercise 3
print('- Exercise 3 -')
print(f"Last two foods: {foods[3:]}")

# Exercise 4
print('- Exercise 4 -')
home_town = {
    'city': 'Toronto',
    'province': 'Ontario',
    'population': 6196731
}

print(
    f"I was born in {home_town['city']}, {home_town['province']} - population of {home_town['population']}.")

# Exercise 5
print('- Exercise 5 -')

home_town.items()

for key, val in home_town.items():
    print(f"{key} = {val}")

# Exercise 6
print('- Exercise 6 -')

cohort = []

for idx, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[idx]
    })

for student in cohort:
    print(student)

# Exercise 7
print('- Exercise 7 -')

awesome_students = [f"{name} is awesome!" for name in students]

for awesome_student in awesome_students:
    print(awesome_student)

# Exercise 8
print('- Exercise 8 -')

# for food in foods:
#     if 'a' in food:
#         print(food)

for food in [food for food in foods if 'a' in food]:
    print(food)
