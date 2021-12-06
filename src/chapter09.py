original_messages = ["Hey you!", "How you doing?", "I don't care."]
sent_messages = []


def send_messages(message_lst):
    print(message_lst)
    for message in message_lst:
        print(message)
        sent_messages.append(message)
        message_lst.remove(message)

send_messages(original_messages)
print(f"Original list: {original_messages}")
print(f"Sent messages list: {sent_messages}")

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""