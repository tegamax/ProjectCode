'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn import module_name as mn
from module_name import *
'''


import func1                            #make_car
from func2 import desired_Sandwiches
from func3 import *                     #send_messages  , show_messages
from func4 import make_album as ma 
import func4 as f4

func1.make_car('Toyota','Rav 4',color='blue')

desired_Sandwiches('Tomatoes','Jalapenos','onions','pickles','cabbage')



messages = ['monitor', 'mouse', 'laptop', 'keyboard']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print(ma('Tiwa Savage', 'Tiwa', 20))

print(f4.make_album('Bella Shmurda', 'High Tension', 16))
