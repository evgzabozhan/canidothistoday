import random

values = ['Yes', 'No']


def get_yes_or_no():
    return random.choice(values)


def generate_massive():
    values_mass = []
    for x in range(5):
        values_mass.append(get_yes_or_no())
    return values_mass


def get_decision():
    mass = generate_massive()
    if mass.count('Yes') > mass.count('No'):
        return 'Yes'
    else:
        return 'No'


print(get_decision())
