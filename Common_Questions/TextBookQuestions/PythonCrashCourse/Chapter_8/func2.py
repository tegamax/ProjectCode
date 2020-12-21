def desired_Sandwiches(*items):
    for item in items:
        print(f'Your sandwich will come with the following ingredients {item}')

desired_Sandwiches('Ranch Sauce')
desired_Sandwiches('Tomatoes','Jalapenos')
desired_Sandwiches('onions','pickles','cabbage')



desired_Sandwiches('Tomatoes','Jalapenos','onions','pickles','cabbage')