'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant:
    '''
    This is a Restaurant class
    '''
    def __init__(self,restaurant_name,cuisine_type):
        "initialize the restaurant_name and the cuisine_type attributes"
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):#style_Of_Restaurant,location):
        print(f'The name of the restaurant is {self.restaurant_name.title()} and the type of cuisine is {self.cuisine_type.title()}.')
        #print(f'The style of the restaurant is {style_Of_Restaurant.title()} and the location is: {location.title}.')
    
    def describe_restaurant2(self):
        print("I'm inside the describe_restaurant function")

    def describe_restaurant3(self,style_Of_Restaurant,location):
        print(f"The restaurant style is a {style_Of_Restaurant} and it is located in {location}")

    def open_restaurant(self,message):
        print(f'The {message.title()} restaurant is now open.')

restaurant = Restaurant('de thomson','steak')
#rest = 'town_house','westchester'

print(f'The name of the restaurant is {restaurant.restaurant_name.title()} and the type of cuisine is {restaurant.cuisine_type.title()}.')
restaurant.describe_restaurant()

restaurant.describe_restaurant3('town_house','westchester') #or Restaurant.describe_restaurant3('town_house','westchester')

Restaurant.open_restaurant("You're welcome to the partake in a free raffle draw")
#or restaurant.open_restaurant("You're welcome to the partake in a free raffle draw"). For this one the function itself will need to have the self instance.
#eg def open_restaurant(self,message):

