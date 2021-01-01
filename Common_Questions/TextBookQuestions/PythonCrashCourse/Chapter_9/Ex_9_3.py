'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
'''


class Users:
    def __init__(self,first_name,last_name,sex,location,occupation,ethnic_background,religious_belifs):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.location = location
        self.occupation = occupation
        self.ethnic_background = ethnic_background
        self.religious_belifs = religious_belifs
        
    def greet_user(self):
        print(f"Hello {self.last_name},{self.first_name}. I see that you're a {self.ethnic_background} {self.sex} from {self.location}. You're also a/an {self.occupation} who is an ardent {self.religious_belifs}!")


User1 = Users('Emeka','Azuh','Male','Lagos','Civil Engineer','Black','Catholic')
User2 = Users('Abibat','Oshiobugie','Female','Lagos','Medical Doctor','Black','Christian')
User3 = Users('Irikefe','Odjiegba','Male','Lagos','Business Man','Black','Christian')
User4 = Users('Annabel','Bench','Female','Illinois','Student','White','Catholic')

User1.greet_user()
User2.greet_user()
User3.greet_user()
User4.greet_user()
