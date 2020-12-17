'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
'''

def send_messages(short_message):
    sent_messages=[]
    while short_message:
        current_message = short_message.pop()
        sent_messages.append(current_message)
        print(f'Original list {short_message}')
        print(f'Updated List {sent_messages}')


messages = ['apple','mango','guava']
print(send_messages(messages))




'''
def send_messages(short_list,sent_messages):
    while short_list:
        curent_message = short_list.pop()
        print(f'THe item {curent_message} is now  removed from short_list')
        sent_messages.append(curent_message)



def printitng_messages(sent_messages):
    for sent_message in sent_messages:
        print(sent_message)


messages = ['monitor','mouse','laptop','keyboard']
sent_messages = []

send_messages(messages,sent_messages)
printitng_messages(sent_messages)
'''