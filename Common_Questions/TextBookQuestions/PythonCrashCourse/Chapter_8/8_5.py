'''
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
'''


def describe_city(city,country='Iceland'):
    cities = ['Reykjavik','Kópavogur','Reykjanesbær','Garðabær','Mosfellsbær','Hafnarfjörður']
    for i in cities:
        if i==city:
            print(f'{i} is in Iceland')
            break
    else:
        print(f'So you think {city} is a city Iceland?')


describe_city('Garðabær','country')



'''
Árborg
Akureyri
'''