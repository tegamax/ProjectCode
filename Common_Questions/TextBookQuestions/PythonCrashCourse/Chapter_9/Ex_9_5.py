'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
'''

class User:
    '''This is a program that checks the number of users in a sysytem'''

    def __init__(self,first_name,last_name,sex,location,occupation,ethnic_background,religious_beliefs,login_attempts,seperators):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.location = location
        self.occupation = occupation
        self.ethnic_background = ethnic_background
        self.religious_beliefs = religious_beliefs
        self.login_attempts = 0
        self.seperators = seperators

    def increment_login_attempts(self):
        self.login_attempts += 1
        #print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        #print(self.login_attempts)
    
    def open_seperators(self):
        print(f"{self.seperators}")


John = User('John','Paul','Male','Abuja','Pilot','Asian','Hindu',0,'-')

John.open_seperators()
John.open_seperators()
John.open_seperators()


print(f"Hello {John.last_name},{John.first_name}. I see that you're a {John.ethnic_background} {John.sex} from {John.location}. You're also a/an {John.occupation} who is an ardent {John.religious_beliefs}!")


John.open_seperators()
John.open_seperators()
John.open_seperators()

John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()
print(f"The user: {John.last_name},{John.first_name} logged into the system {John.login_attempts} times")


John.open_seperators()
John.open_seperators()
John.open_seperators()

John.reset_login_attempts()
print(f"The login attempts for the following user: {John.last_name},{John.first_name}, has been reset to {John.login_attempts}")