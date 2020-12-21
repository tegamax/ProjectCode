def show_messages(messages):
    print("Printing all messages")
    for message in messages:
        print(message)


def send_messages(messages,sent_messages):
    while messages:
        removed_messages = messages.pop()
        sent_messages.append(removed_messages)
        print(sent_messages)



