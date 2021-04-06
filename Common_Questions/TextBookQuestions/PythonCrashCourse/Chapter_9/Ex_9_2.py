
'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, 
and call describe_restaurant() for each instance.
'''

class Restaurant:
    '''this is the reataurant class'''
    def __init__(self,restaurant_name,cuisine_type,location):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}, they serve {self.cuisine_type} cuisine and they are located in {self.location}.")



#Three instances were created from the class
my_restaurant = Restaurant('Eureka','American','Mountain View')
my_restaurant.describe_restaurant()

