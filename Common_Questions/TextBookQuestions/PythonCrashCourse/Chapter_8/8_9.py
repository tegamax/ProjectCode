'''
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''



'''
def show_messages(short_message):
    print(short_message + '\n')

messages = [" \"The greatest glory in living lies not in never falling, but in rising every time we fall.\" -Nelson Mandela",
" \"The way to get started is to quit talking and begin doing.\" -Walt Disney",
" \"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.\" -Steve Jobs",
" \"If life were predictable it would cease to be life, and be without flavor.\" -Eleanor Roosevelt",
" \"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.\" -Oprah Winfrey",
" \"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.\" -James Cameron ",
" \"Life is what happens when you're busy making other plans.\" -John Lennon "]

for i in messages:
    show_messages(i)
'''





def show_messages(short_message):
    for i in short_message:
        print(i +'\n')


messages = [" \"The greatest glory in living lies not in never falling, but in rising every time we fall.\" -Nelson Mandela",
    " \"The way to get started is to quit talking and begin doing.\" -Walt Disney",
    " \"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.\" -Steve Jobs",
    " \"If life were predictable it would cease to be life, and be without flavor.\" -Eleanor Roosevelt",
    " \"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.\" -Oprah Winfrey",
    " \"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.\" -James Cameron ",
    " \"Life is what happens when you're busy making other plans.\" -John Lennon "]
print(show_messages(messages))