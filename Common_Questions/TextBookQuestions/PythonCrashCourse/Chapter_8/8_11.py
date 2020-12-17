'''
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
'''


'''
def send_messages(short_list):
    sent_messages = []
    current_message = short_list.pop()
    sent_messages.append(current_message)
    #print(sent_messages)

messages = ['monitor','mouse','laptop','keyboard']
send_messages(messages)
print(messages)

'''


'''
def send_messages(short_list):
    sent_messages = []
    current_message = short_list.pop()
    sent_messages.append(current_message)
    return sent_messages


messages = ['monitor', 'mouse', 'laptop', 'keyboard']
#sent_messages = []
#send_messages(messages[:])
print(messages[:])

'''

def show_messages(messages):
    print("Printing all messages")
    for message in messages:
        print(message)


def send_messages(messages,sent_messages):
    while messages:
        removed_messages = messages.pop()
        sent_messages.append(removed_messages)
        print(sent_messages)

messages = ['monitor', 'mouse', 'laptop', 'keyboard']
show_messages(messages)


sent_messages = []
send_messages(messages[:], sent_messages)


