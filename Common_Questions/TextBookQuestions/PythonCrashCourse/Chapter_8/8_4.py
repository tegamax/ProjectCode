

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
'''

'''
def make_shirt(shirt_size='large'):
    if shirt_size == 'large':
        print('I love Python')
'''


def make_shirt(shirt_size):
    if shirt_size == 'large' or shirt_size == 'medium':
        print('I love Python')
    else:
        print('we all love python')

#make_shirt('small')
#make_shirt('large')
make_shirt('medium')