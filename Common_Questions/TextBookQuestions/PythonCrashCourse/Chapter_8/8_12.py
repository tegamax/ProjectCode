'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
'''

def desired_Sandwiches(*items):
    for item in items:
        print(f'Your sandwich will come with the following ingredients {item}')

desired_Sandwiches('Ranch Sauce')
desired_Sandwiches('Tomatoes','Jalapenos')
desired_Sandwiches('onions','pickles','cabbage')

#sandwich_items('Tomatoes','Jalapenos','onions','pickles','cabbage')

