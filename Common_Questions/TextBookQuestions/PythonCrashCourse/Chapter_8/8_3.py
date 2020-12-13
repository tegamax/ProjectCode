'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

'''

size=input('please enter the size of the shirt: ')
message=input('Please enter a message to be printed on the shirt: ')

def make_shirt(size,message):
    print(f'The shirt is of size {size.title()} with message: {message}')

make_shirt(size,message)


#This is the day that makes us proud